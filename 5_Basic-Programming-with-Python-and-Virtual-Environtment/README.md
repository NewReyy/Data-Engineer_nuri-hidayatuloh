### Resume

Python and Virtual Environment:

- **Python Virtual Enironment**: Virtual Envirinment adalah sebuah tools atau alat untuk membantu memisahkan dependensi yang diperlukan oleh proyek berbeda dengan membuat virtual environment terisolasi untuk proyek tersebut. Ini merupakan salah satu alat terpenting yang digunakan sebagian besar Developer Python.   

- Diciptakan untuk **memisahkan dependensi** yang diperlukan oleh satu proyek Python dari proyek Python lainnya.
- **Mencegah konflik dependensi**, memastikan bahwa setiap proyek memiliki lingkungan kerja yang terisolasi.

- Digunakan ketika **mengembangkan atau menjalankan proyek Python** untuk memastikan keseragaman dan menghindari konflik dependensi.

- Virtual Environment diimplementasikan **di dalam direktori proyek Python** dan bersifat lokal untuk proyek tersebut.

- Dibuat menggunakan **perintah-perintah seperti `venv`** atau menggunakan alat manajemen lingkungan seperti **`virtualenv` atau `conda`**.
- **Mengisolasi** lingkungan Python dengan membuat salinan dari interpreter dan pustaka standar.

Untuk menginstall dan menggunakan `venv` (Virtual Environment) di Windows, Anda dapat mengikuti langkah-langkah berikut:

1. **Buka Command Prompt:**
   - Tekan `Win + R` untuk membuka jendela "Run".
   - Ketik `cmd` dan tekan Enter.

2. **Pastikan Python Terinstall:**
   - Pastikan Python sudah terinstall di laptop atau sistem. Anda dapat memeriksa dengan menjalankan perintah `python --version` atau `python -V` di Command Prompt.

3. **Buat Virtual Environment:**
   - Pilih atau buat direktori tempat Anda ingin menyimpan virtual environment. Pindah ke direktori tersebut dengan perintah `cd path\to\your\directory`.

   - Jalankan perintah berikut untuk membuat virtual environment:
     ```
     python -m venv venv
     ```
     Di sini, `venv` adalah nama folder untuk virtual environment. Dan dapat menggantinya sesuai kebutuhan.

4. **Aktifkan Virtual Environment:**
   - Di dalam direktori tempat virtual environment dibuat, jalankan perintah untuk mengaktifkannya:
     - Untuk Command Prompt:
       ```
       venv\Scripts\activate
       ```
     - Untuk PowerShell:
       ```
       .\venv\Scripts\Activate
       ```

   - Jika aktivasi berhasil, akan terlihat nama virtual environment di prompt.

5. **Deaktivasi Virtual Environment:**
   - Kapan pun ingin keluar dari virtual environment, jalankan perintah:
     ```
     deactivate
     ```