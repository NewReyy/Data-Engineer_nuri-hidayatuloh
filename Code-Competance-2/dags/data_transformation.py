import pandas as pd
import os
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, storage
import logging

class DataWarehouseLoader:
    def __init__(self):
        # Inisialisasi kredensial Firebase dan koneksi ke bucket storage
        cred = credentials.Certificate(r"cc2AccountKey.json")
        firebase_admin.initialize_app(cred, {
            "storageBucket": "codecompetance2-nuri.appspot.com"
        })
        self.bucket = storage.bucket()
        
        # Setup logger
        self.logger = self._setup_logger()

    def _setup_logger(self):
        # Setup logger dengan level INFO
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        # Format log dan tambahkan handler untuk log ke konsol
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

        return logger

    def load_data(self, file_path):
        try:
            # Load data dari file parquet
            df = pd.read_parquet(file_path)
            self.logger.info(f"Data berhasil dimuat dari {file_path}")
            return df
        except Exception as e:
            # Tangani kesalahan jika gagal memuat data
            self.logger.error(f"Gagal memuat data dari {file_path}: {e}")
            return None

    def transform_data(self, df_transactions, df_tickets, df_events, df_customer_feedback):
        # Gabungkan dataframe sesuai kebutuhan
        merged_df = pd.merge(df_transactions, df_tickets, on='ticket_id', how='inner')
        merged_df = pd.merge(merged_df, df_events, on='event_id', how='inner')

        # Hitung total tiket terjual per acara
        tickets_sold_per_event = merged_df.groupby('event_id')['quantity'].sum().reset_index()
        tickets_sold_per_event.columns = ['event_id', 'tickets_sold']

        # Hitung total pendapatan per acara
        revenue_per_event = merged_df.groupby('event_id')['total_amount'].sum().reset_index()

        # Hitung rata-rata rating per acara jika kolom 'transaction_id' ada dalam dataframe customer_feedback
        if 'transaction_id' in df_customer_feedback.columns:
            feedback_analysis = pd.merge(df_customer_feedback, df_transactions, on='transaction_id', how='inner')
            avg_rating_per_event = feedback_analysis.groupby('feedback_id')['rating'].mean().reset_index()
            self.logger.info("Berhasil Menghitung Rata-rata rating per-Acara")
            self.logger.info(f"Berikut adalah Rata-rata Rating per-Acara: \n{avg_rating_per_event}")
        else:
            avg_rating_per_event = pd.DataFrame()

        # Log pesan jika kolom 'transaction_id' tidak ditemukan dalam dataframe customer_feedback
        if 'transaction_id' not in df_customer_feedback.columns:
            self.logger.warning("Kolom 'transaction_id' tidak ditemukan dalam dataframe customer_feedback.")

        return tickets_sold_per_event, revenue_per_event, avg_rating_per_event

    def save_to_warehouse(self, df, table_name):
        if df is not None and not df.empty:
            try:
                # Simpan dataframe ke file parquet dan unggah ke Firebase Storage
                current_date = datetime.now().strftime('%Y/%m/%d')
                os.makedirs(current_date, exist_ok=True)

                file_name = f"{current_date}/{table_name}.parquet"
                df.to_parquet(file_name, index=False)
                blob = self.bucket.blob(file_name)
                blob.upload_from_filename(file_name)
                self.logger.info(f"Data berhasil disimpan ke Firebase Storage: {file_name}")
                os.remove(file_name)  # Hapus file lokal setelah diunggah
            except Exception as e:
                # Tangani kesalahan jika gagal menyimpan data
                self.logger.error(f"Gagal menyimpan data ke Firebase Storage: {e}")
        else:
            # Beri peringatan jika dataframe kosong
            self.logger.warning(f"Tidak ada data yang akan disimpan untuk tabel: {table_name}")

if __name__ == "__main__":
    loader = DataWarehouseLoader()

    events_df = loader.load_data('Code-Competance-2/data_source/events.parquet')
    customers_df = loader.load_data('Code-Competance-2/data_source/customers.parquet')
    tickets_df = loader.load_data('Code-Competance-2/data_source/tickets.parquet')
    transactions_df = loader.load_data('Code-Competance-2/data_source/transactions.parquet')
    customer_feedback_df = loader.load_data('Code-Competance-2/data_source/customer_feedback.parquet')

    tickets_sold, revenue, avg_rating = loader.transform_data(transactions_df, tickets_df, events_df, customer_feedback_df)

    loader.save_to_warehouse(tickets_sold, 'tickets_sold_per_event')
    loader.save_to_warehouse(revenue, 'revenue_per_event')
    loader.save_to_warehouse(avg_rating, 'avg_rating_per_event')