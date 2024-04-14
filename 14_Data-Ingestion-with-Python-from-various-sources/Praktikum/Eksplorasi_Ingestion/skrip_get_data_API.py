import csv
import requests

# Mengirim permintaan HTTP
url = "https://gist.githubusercontent.com/nadirbslmh/8922f71875948802321ef479a017f4c0/raw/1fbbc4b3d55f8ae717eb197d9aaf530ed1bc7ed2/sample.json"
response = requests.get(url)

# Memeriksa status respons
if response.status_code == 200:
    # Mengambil data JSON
    data = response.json()
    
    # Memeriksa apakah kunci 'data' ada dalam respons JSON
    if "data" in data:
        # Mendapatkan daftar buku
        books = data["data"]
        
        # Menyimpan informasi buku ke dalam file CSV
        with open("books.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["Judul", "Pengarang", "Tahun Terbit", "Genre"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Menulis header
            writer.writeheader()
            
            # Menulis baris untuk setiap buku
            for book in books:
                writer.writerow({
                    "Judul": book["title"],
                    "Pengarang": book["author"],
                    "Tahun Terbit": book["year"],
                    "Genre": book["genre"]
                })
        print("Data telah disimpan dalam file 'books.csv'")
    else:
        print("Kunci 'data' tidak ditemukan dalam respons JSON.")
else:
    print("Gagal mengambil data. Status code:", response.status_code)