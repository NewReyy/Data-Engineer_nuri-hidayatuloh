REST API

1. API & REST API
- API merupakan singkatan dari "Application Programming Interface". Secara sederhana, API adalah sebuah metode komunikasi antara satu aplikasi dengan satu atau banyak aplikasi lainnya. Rancangan dan implementasi APi mengikuti suatu set protokol atau spesifikasi sehingga memungkinkan sebuah aplikasi bisa melakuka request sebuah proses ataupun data ke aplikasi lainnya.
- Sebagaimana contoh, Client diibaratkan sebagai pengguna yang memberikan Request kepada Waiter yang mana Waiter dalam sistem ini berperan sebagai **API** nya lalu waiter tersebut menerusnya Request dari Client tersebut terhadap Chef yang mana Chef disini diibaratkan sebagai System/Server yang akan memberikan Response dari Request yang diberikan oleh Waiter dan Waiter akan meneruskan Response dari Chef tersebut kepada Client.
- Benefit membuat atau menggunakan API :
	Dengan Memanfaatkan APi, developmeny sebuah produk digital akan relatif lebih mudah, cepat dan maintainable.
	- Sebuah proses atau fungsi cukup dikembangkan di satu tempat dan dapat digunakan diberbagai aplikasi.
	- Bisa memanfaatkan API yang disediakan 3rd party untuk proses-proses yang kompleks seperti AI dan Ml, seperti Google Vision API atau Speech to Text.

**Testing API:**
Pengujian API adalah proses untuk memastikan bahwa antarmuka pemrograman aplikasi (API) berfungsi sesuai yang diharapkan. Ini termasuk verifikasi fungsionalitas, kinerja, keamanan, dan keandalan dari API. Contoh pengujian API meliputi:
- Pengujian fungsional untuk memastikan API memberikan respons yang benar sesuai dengan spesifikasi.
- Pengujian kinerja untuk mengevaluasi kinerja API dalam situasi beban tinggi.
- Pengujian keamanan untuk mengidentifikasi potensi celah keamanan atau kerentanan.
- Pengujian keandalan untuk menentukan apakah API dapat bertahan pada situasi yang tidak terduga.

**Contoh Implementasi API:**
Implementasi API dapat ditemukan dalam berbagai konteks, seperti:
- Penerapan API oleh penyedia layanan seperti Google Maps API yang memungkinkan pengembang untuk mengintegrasikan peta dalam aplikasi mereka.
- Pengembangan aplikasi klien seperti aplikasi mobile yang menggunakan API Twitter untuk menampilkan feed pengguna.

**API Protocol dan Architectures:**
Protokol umum untuk API termasuk REST (Representational State Transfer) dan GraphQL. REST adalah pendekatan arsitektur yang sering digunakan untuk mengembangkan web API berbasis HTTP, sementara GraphQL adalah bahasa kueri yang memungkinkan klien untuk mendefinisikan struktur data yang mereka butuhkan. Arsitektur umum untuk API meliputi RESTful API, SOAP (Simple Object Access Protocol), dan RPC (Remote Procedure Call).

**REST API:**
REST API adalah gaya arsitektur untuk pembangunan API di internet berbasis pada prinsip-prinsip REST. Contoh REST API adalah Twitter API, yang memungkinkan pengembang untuk mengakses data pengguna dan tweet melalui permintaan HTTP.

**HTTP Methods:**
Metode HTTP (HTTP methods) digunakan untuk menentukan jenis operasi yang diinginkan terhadap sumber daya yang ditentukan. Contoh HTTP methods termasuk:
- GET: Mengambil data dari sumber daya.
- POST: Membuat data baru.
- PUT: Memperbarui data yang ada.
- DELETE: Menghapus data.

**HTTP Response Code:**
Kode respons HTTP memberikan informasi tentang hasil dari permintaan HTTP. Contoh kode respons termasuk:
- 200 (OK): Permintaan berhasil.
- 404 (Not Found): Sumber daya yang diminta tidak ditemukan.
- 500 (Internal Server Error): Terjadi kesalahan pada server.

**Rest API Component & Headers:**
Komponen utama REST API meliputi endpoint, metode HTTP, dan badan (body) pesan. Header HTTP menyediakan informasi tambahan tentang permintaan atau respons. Contoh header HTTP termasuk Content-Type untuk menentukan tipe konten dan Authorization untuk otorisasi.

**JSON:**
JSON adalah format pertukaran data yang ringan dan mudah dibaca. Contoh JSON adalah:
```json
{
  "name": "John",
  "age": 30,
  "city": "New York"
}
```

**Cara Menggunakannya di Postman:**
Postman adalah aplikasi pengembangan API yang memungkinkan pengguna untuk membuat, menguji, dan memantau API. Contoh penggunaan Postman termasuk membuat permintaan HTTP ke endpoint API, menentukan metode HTTP, dan mengevaluasi respons.

**Keuntungan API:**
Keuntungan menggunakan API termasuk integrasi antara aplikasi dan layanan pihak ketiga, pemisahan logika bisnis dari antarmuka pengguna, dan meningkatkan fleksibilitas serta skalabilitas aplikasi.

**Tantangan API:**
Tantangan dalam menggunakan API termasuk masalah keamanan seperti penyusupan, pengelolaan versi dan dokumentasi API, memastikan ketersediaan dan kinerja yang tinggi, dan menangani perubahan pada sumber daya dan permintaan pengguna.