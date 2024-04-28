import os
import pandas as pd
import numpy as np
import logging

class DataLakeBuilder:
    def __init__(self):
        self.logger = self._setup_logger()  # Inisialisasi logger saat objek DataLakeBuilder dibuat

    def _setup_logger(self):
        logger = logging.getLogger('DataLakeBuilder')  # Buat objek logger dengan nama 'DataLakeBuilder'
        logger.setLevel(logging.INFO)  # Set level logger ke INFO
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # Format pesan log
        stream_handler = logging.StreamHandler()  # Handler untuk menampilkan log di konsol
        stream_handler.setFormatter(formatter)  # Set formatter untuk handler
        logger.addHandler(stream_handler)  # Tambahkan handler ke logger
        return logger

    def read_csv_data(self, file_path):
        try:
            return pd.read_csv(file_path)  # Baca file CSV dan kembalikan DataFrame
        except Exception as e:
            self.logger.error(f"Error reading CSV file {file_path}: {e}")  # Tangani kesalahan jika gagal membaca file
            return None
    
    def handle_missing_values(self, df):
        try:
            numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()  # Ambil nama kolom numerik
            df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())  # Isi nilai yang hilang dengan rata-rata
            return df
        except Exception as e:
            self.logger.error(f"Error handling missing values: {e}")  # Tangani kesalahan jika gagal menangani nilai yang hilang
            return None
    
    def handle_outliers(self, df, column, method='median'):
        try:
            Q1 = df[column].quantile(0.25)  # Kuartil pertama
            Q3 = df[column].quantile(0.75)  # Kuartil ketiga
            IQR = Q3 - Q1  # Rentang interkuartil
            lower_bound = Q1 - 1.5 * IQR  # Batas bawah
            upper_bound = Q3 + 1.5 * IQR  # Batas atas
            if method == 'median':
                df[column] = np.where((df[column] < lower_bound) | (df[column] > upper_bound), df[column].median(), df[column])  # Tangani outlier dengan median
            elif method == 'mean':
                df[column] = np.where((df[column] < lower_bound) | (df[column] > upper_bound), df[column].mean(), df[column])  # Tangani outlier dengan mean
            else:
                self.logger.warning("Invalid method for handling outliers. Using median instead.")
                df[column] = np.where((df[column] < lower_bound) | (df[column] > upper_bound), df[column].median(), df[column])  # Tangani outlier dengan median jika metode tidak valid
            return df
        except Exception as e:
            self.logger.error(f"Error handling outliers: {e}")  # Tangani kesalahan jika gagal menangani outlier
            return None
    
    def handle_duplicates(self, df):
        try:
            df.drop_duplicates(inplace=True)  # Hapus baris duplikat
            return df
        except Exception as e:
            self.logger.error(f"Error handling duplicates: {e}")  # Tangani kesalahan jika gagal menangani duplikat
            return None
    
    def save_to_parquet(self, df, file_name):
        try:
            df.to_parquet(file_name)  # Simpan DataFrame ke file Parquet
            self.logger.info(f"Saved DataFrame to Parquet file: {file_name}")  # Log pesan jika penyimpanan berhasil
        except Exception as e:
            self.logger.error(f"Error saving DataFrame to Parquet file: {e}")  # Tangani kesalahan jika gagal menyimpan ke file Parquet
    
    def validate_data(self, file_path):
        try:
            df = pd.read_parquet(file_path)  # Baca file Parquet
            self.logger.info(f"Ringkasan Data dari file {file_path}:")  # Log pesan
            self.logger.info(df.head())  # Tampilkan beberapa baris pertama DataFrame
            self.logger.info("\n" + df.describe().to_string())  # Tampilkan ringkasan statistik
            self.logger.info("\n")
        except Exception as e:
            self.logger.error(f"Error validating data: {e}")  # Tangani kesalahan jika gagal validasi data


if __name__ == "__main__":
    builder = DataLakeBuilder()

    folder_path = 'Code-Competance-2/data_source'

    csv_files = os.listdir(folder_path)
    for csv_file in csv_files:
        if csv_file.endswith('.csv'):
            csv_file_path = os.path.join(folder_path, csv_file)
            parquet_file_path = os.path.splitext(csv_file_path)[0] + '.parquet'

            data = builder.read_csv_data(csv_file_path)
            if data is not None:
                data = builder.handle_missing_values(data)
                if data is not None and 'amount' in data.columns:
                    data = builder.handle_outliers(data, 'amount')
                data = builder.handle_duplicates(data)
                if data is not None:
                    builder.save_to_parquet(data, parquet_file_path)
                    builder.validate_data(parquet_file_path)