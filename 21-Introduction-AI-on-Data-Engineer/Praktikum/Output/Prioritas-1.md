Tentu, berikut adalah contoh sederhana dari DDL (Data Definition Language) dan DML (Data Manipulation Language) untuk membuat sebuah database praktikum. Kita akan membuat database untuk memantau karyawan dan proyek-proyek yang sedang dikerjakan oleh mereka. Mari kita mulai dengan DDL untuk membuat struktur database:

DDL (Data Definition Language):

```sql
-- Membuat database praktikum
CREATE DATABASE IF NOT EXISTS praktikum;

-- Menggunakan database praktikum
USE praktikum;

-- Membuat tabel karyawan
CREATE TABLE IF NOT EXISTS karyawan (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(100) NOT NULL,
    posisi VARCHAR(50) NOT NULL,
    departemen VARCHAR(50),
    gaji DECIMAL(10, 2),
    tanggal_masuk DATE
);

-- Membuat tabel proyek
CREATE TABLE IF NOT EXISTS proyek (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama_proyek VARCHAR(100) NOT NULL,
    deskripsi TEXT,
    status ENUM('Pending', 'In Progress', 'Completed') DEFAULT 'Pending',
    deadline DATE
);

-- Membuat tabel penugasan
CREATE TABLE IF NOT EXISTS penugasan (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_karyawan INT,
    id_proyek INT,
    tanggal_mulai DATE,
    tanggal_selesai DATE,
    FOREIGN KEY (id_karyawan) REFERENCES karyawan(id),
    FOREIGN KEY (id_proyek) REFERENCES proyek(id)
);
```

Sekarang, mari kita masukkan beberapa data contoh menggunakan DML (Data Manipulation Language):

DML (Data Manipulation Language):

```sql
-- Memasukkan data karyawan
INSERT INTO karyawan (nama, posisi, departemen, gaji, tanggal_masuk) VALUES
('John Doe', 'Software Engineer', 'Engineering', 5000.00, '2020-01-15'),
('Jane Smith', 'Data Analyst', 'Analytics', 4500.00, '2019-08-20'),
('Michael Johnson', 'Project Manager', 'Management', 6000.00, '2018-05-10');

-- Memasukkan data proyek
INSERT INTO proyek (nama_proyek, deskripsi, status, deadline) VALUES
('Sistem Manajemen Inventaris', 'Membangun sistem manajemen inventaris perusahaan', 'In Progress', '2024-06-30'),
('Analisis Data Pelanggan', 'Analisis data pelanggan untuk mendapatkan wawasan pasar', 'Pending', '2024-07-15');

-- Memasukkan data penugasan
INSERT INTO penugasan (id_karyawan, id_proyek, tanggal_mulai, tanggal_selesai) VALUES
(1, 1, '2024-02-01', NULL),
(2, 1, '2024-03-15', NULL),
(3, 2, '2024-04-01', NULL);
```

Dengan DDL di atas, kita membuat struktur database dengan tiga tabel: karyawan, proyek, dan penugasan. Kemudian, dengan DML, kita memasukkan beberapa data contoh ke dalam tabel-tabel tersebut. Kamu bisa menyesuaikan struktur dan data sesuai kebutuhan praktikum atau proyek tertentu. Apakah ada yang bisa saya jelaskan lebih lanjut?