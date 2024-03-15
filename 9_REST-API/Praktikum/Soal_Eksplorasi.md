### Soal **Eksplorasi (20)**

1. Eksplorasi API RentABook:
    - Pelajari dokumentasi API dari RentABook: **https://app.swaggerhub.com/apis-docs/sepulsa/RentABook-API/1.0.0**.
    - Identifikasi endpoint yang tersedia dan fungsinya.
    Dalam API RentABook, berdasarkan identifikasi yang Anda berikan, berikut adalah endpoint-endpoint yang tersedia beserta fungsinya:

1. **Authentication (Autenthication)**:
   - **/auth/token (GET)**: Digunakan untuk meminta atau mendapatkan token akses.

2. **Client (Client)**: 
   - **GET /client/{id}**: Mengambil data klien berdasarkan ID.
   - **PUT /client/{id}**: Memperbarui data klien.
   - **DELETE /client/{id}**: Menghapus klien.
   - **GET /client**: Mendapatkan semua klien.
   - **POST /client**: Menambahkan klien baru.

3. **User (User)**:
   - **/users (GET)**: Mengembalikan daftar semua pengguna.
   - **/users/{id} (GET)**: Mengembalikan informasi detail pengguna berdasarkan ID.
   - **/users/{id} (PUT)**: Digunakan untuk memperbarui informasi pengguna berdasarkan ID.
   - **/users/{id} (DELETE)**: Digunakan untuk menghapus pengguna berdasarkan ID.

4. **Book (Book)**:
   - **/books (GET)**: Mengembalikan daftar semua buku yang tersedia untuk disewa.
   - **/books/{id} (GET)**: Mengembalikan detail buku berdasarkan ID.
   - **/books/search (GET)**: Digunakan untuk mencari buku berdasarkan judul atau penulis.
   - **/books (POST)**: Digunakan untuk menambahkan buku baru.
   - **/books/{id} (PUT)**: Digunakan untuk memperbarui detail buku berdasarkan ID.
   - **/books/{id} (DELETE)**: Digunakan untuk menghapus buku berdasarkan ID.

5. **Rent (Rent)**:
   - **GET /rent/{id}**: Mendapatkan transaksi penyewaan buku berdasarkan ID.
   - **GET /rent**: Mendapatkan semua transaksi penyewaan buku.
   - **POST /rent**: Menyewa sebuah buku.

2. Implementasi 4 Method pada RentABook API:
    - Lakukan request dengan method GET, POST, PUT, dan DELETE pada endpoint yang tersedia di RentABook API.
    - Contoh: Lakukan operasi CRUD pada resource client.
    - **GET**:
    ![alt text](../Screenshots/Hasil_Eksplorasi(GET-REQUEST).png)
    ![alt text](../Screenshots/Hasil_Eksplorasi(GET-REQUEST-ID1-HEADERSRESPONSE).png)
    ![alt text](../Screenshots/Hasil_Eksplorasi(GET-REQUEST-ID1-BODYRESPONSE).png)

    - **POST**:
    ![alt text](../Screenshots/Hasil_Eksplorasi(POST-REQUEST).png)

    - **PUT**:
    ![alt text](../Screenshots/Hasil_Eksplorasi(PUT-REQUEST).png)

    - **DELETE**:
    ![alt text](../Screenshots/Hasil_Eksplorasi(DELETE-REQUEST).png)
    
3. Dokumentasi Eksplorasi:
    - Simpan semua request dan response yang berkaitan dengan RentABook API dalam Postman Collection baru.