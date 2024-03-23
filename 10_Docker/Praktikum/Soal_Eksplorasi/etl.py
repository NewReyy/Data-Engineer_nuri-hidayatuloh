import os
import requests
import mysql.connector


# Fungsi untuk mengirim permintaan ke API dan mengembalikan data posting
def ambil_data_post():
    url_api = "https://jsonplaceholder.typicode.com/posts?userId=1"
    respons = requests.get(url_api)
    data = respons.json()
    return data


# Fungsi untuk memasukkan data posting ke dalam tabel MySQL
def masukkan_ke_mysql(posts):
    try:
        # Ganti parameter koneksi dengan detail database MySQL Anda
        koneksi = mysql.connector.connect(
            host=os.environ.get("DB_HOST"),
            user=os.environ.get("DB_USERNAME"),
            password=os.environ.get("DB_PASSWORD"),
            database=os.environ.get("DB_NAME"),
        )

        kursor = koneksi.cursor()

        # Buat tabel posts jika belum ada
        kursor.execute(
            """
            CREATE TABLE IF NOT EXISTS posts (
                id INT AUTO_INCREMENT PRIMARY KEY,
                userId INT,
                title VARCHAR(255),
                body TEXT
            )
        """
        )

        # Masukkan data posting ke dalam tabel
        for post in posts:
            kursor.execute(
                """
                INSERT INTO posts (userId, title, body)
                VALUES (%s, %s, %s)
            """,
                (post["userId"], post["title"], post["body"]),
            )

        koneksi.commit()
        print("Data berhasil dimasukkan ke dalam MySQL")

        kursor.close()
        koneksi.close()

    except mysql.connector.Error as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    # Langkah 1: Ambil data posting dari API
    data_posting = ambil_data_post()

    # Langkah 2: Ekstrak informasi yang relevan dan masukkan ke dalam MySQL
    if data_posting:
        add_data = [
            {
                "userId": user["userId"],  # Ganti "userId" dengan field yang sesuai dengan API
                "title": user["title"],    # Ganti "title" dengan field yang sesuai dengan API
                "body": user["body"]  
            }
            for user in data_posting
        ]
        masukkan_ke_mysql(add_data)
    else:
        print("Tidak ada data posting yang diperoleh dari API.")