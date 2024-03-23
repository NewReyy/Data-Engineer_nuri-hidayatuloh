import pandas as pd

def baca_data_dari_csv(nama_file):
    return pd.read_csv(nama_file)

def preprocessing_data(data):
    # Menghapus baris yang mengandung nilai kosong
    data = data.dropna()

    return data

def tampilkan_data(data):
    print(data)

def main():
    nama_file_csv = 'data.csv'
    data = baca_data_dari_csv(nama_file_csv)
    
    # Preprocessing data
    data = preprocessing_data(data)

    # Menampilkan data setelah preprocessing
    tampilkan_data(data)

if __name__ == "__main__":
    main()