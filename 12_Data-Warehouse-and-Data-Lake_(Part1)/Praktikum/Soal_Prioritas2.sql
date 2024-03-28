docker network create citus-cluster-2

docker run -d --name=citus_coordinator_sewa_kendaraan --net=citus-cluster-a -p 5434:5432 -e POSTGRES_PASSWORD=mypass citusdata/citus

docker run -d --name=citus_sewa_1 --net=citus-cluster-2 -e POSTGRES_PASSWORD=mypass citusdata/citus

docker run -d --name=citus_sewa_2 --net=citus-cluster-2 -e POSTGRES_PASSWORD=mypass citusdata/citus

docker run -e POSTGRES_HOST_AUTH_METHOD=trust -d postgres

docker exec -it citus_coordinator_sewa_kendaraan psql -U postgres

select * from citus_get_active_worker_nodes();

select * from master_add_node('citus_sewa_1', 5432);

select * from master_add_node('citus_sewa_2', 5432);

CREATE TABLE Pelanggan (
    ID_Pelanggan SERIAL PRIMARY KEY,
    Nama_Pelanggan VARCHAR(100),
    Alamat VARCHAR(255),
    Nomor_Telepon VARCHAR(15),
    Email VARCHAR(100)
);

-- Data dummy untuk tabel Pelanggan
INSERT INTO Pelanggan (Nama_Pelanggan, Alamat, Nomor_Telepon, Email) VALUES
('Budi Santoso', 'Jl. Merdeka No. 10', '081234567890', 'budi@example.com'),
('Anita Wijaya', 'Jl. Pahlawan No. 5', '082345678901', 'anita@example.com'),
('Dewi Setiawan', 'Jl. Diponegoro No. 8', '083456789012', 'dewi@example.com'),
('Fajar Pratama', 'Jl. Gajah Mada No. 15', '084567890123', 'fajar@example.com'),
('Citra Utami', 'Jl. Sudirman No. 20', '085678901234', 'citra@example.com'),
('Andi Kusuma', 'Jl. Thamrin No. 25', '086789012345', 'andi@example.com'),
('Siti Rahayu', 'Jl. Hayam Wuruk No. 30', '087890123456', 'siti@example.com'),
('Eko Wibowo', 'Jl. Asia Afrika No. 35', '088901234567', 'eko@example.com'),
('Nina Hasanah', 'Jl. Veteran No. 40', '089012345678', 'nina@example.com'),
('Rudi Hermawan', 'Jl. Kalimantan No. 45', '089123456789', 'rudi@example.com'),
('Agus Surya', 'Jl. Bali No. 50', '089234567890', 'agus@example.com'),
('Sinta Indah', 'Jl. Malang No. 55', '089345678901', 'sinta@example.com'),
('Joko Widodo', 'Jl. Solo No. 60', '089456789012', 'joko@example.com'),
('Wulan Septiani', 'Jl. Semarang No. 65', '089567890123', 'wulan@example.com'),
('Ahmad Basuki', 'Jl. Surabaya No. 70', '089678901234', 'ahmad@example.com'),
('Sari Wijaya', 'Jl. Medan No. 75', '089789012345', 'sari@example.com'),
('Ratna Dewi', 'Jl. Batam No. 80', '089890123456', 'ratna@example.com'),
('Bayu Nugroho', 'Jl. Makassar No. 85', '089901234567', 'bayu@example.com'),
('Nadia Fitri', 'Jl. Bandung No. 90', '089012345678', 'nadia@example.com'),
('Adi Wijaya', 'Jl. Yogyakarta No. 95', '089123456789', 'adi@example.com'),
('Wahyu Prasetyo', 'Jl. Aceh No. 100', '089234567890', 'wahyu@example.com'),
('Putri Ananda', 'Jl. Manado No. 105', '089345678901', 'putri@example.com'),
('Rizki Rahman', 'Jl. Padang No. 110', '089456789012', 'rizki@example.com'),
('Yoga Saputra', 'Jl. Palembang No. 115', '089567890123', 'yoga@example.com'),
('Dita Cahyani', 'Jl. Bengkulu No. 120', '089678901234', 'dita@example.com'),
('Irfan Saputro', 'Jl. Lampung No. 125', '089789012345', 'irfan@example.com'),
('Ayu Setiawan', 'Jl. Banten No. 130', '089890123456', 'ayu@example.com'),
('Doni Purnama', 'Jl. Samarinda No. 135', '089901234567', 'doni@example.com'),
('Lina Wati', 'Jl. Banjarmasin No. 140', '089012345678', 'lina@example.com'),
('Eka Prasetya', 'Jl. Ambon No. 145', '089123456789', 'eka@example.com'),
('Reza Ramadhan', 'Jl. Singaraja No. 150', '089234567890', 'reza@example.com'),
('Cindy Putri', 'Jl. Denpasar No. 155', '089345678901', 'cindy@example.com'),
('Feri Yanto', 'Jl. Mataram No. 160', '089456789012', 'feri@example.com'),
('Ratih Pertiwi', 'Jl. Pontianak No. 165', '089567890123', 'ratih@example.com'),
('Dewa Aditya', 'Jl. Batu No. 170', '089678901234', 'dewa@example.com'),
('Rina Susanti', 'Jl. Kupang No. 175', '089789012345', 'rina@example.com'),
('Rudy Kusuma', 'Jl. Jayapura No. 180', '089890123456', 'rudy@example.com'),
('Dini Pratiwi', 'Jl. Gorontalo No. 185', '089901234567', 'dini@example.com'),
('Agung Nugraha', 'Jl. Jambi No. 190', '089012345678', 'agung@example.com'),
('Rini Permata', 'Jl. Pekanbaru No. 195', '089123456789', 'rini@example.com'),
('Eko Saputra', 'Jl. Manokwari No. 200', '089234567890', 'eko_s@example.com'),
('Indra Wijaya', 'Jl. Makasar No. 205', '089345678901', 'indra_w@example.com'),
('Yuli Kurniawan', 'Jl. Ambon No. 210', '089456789012', 'yuli@example.com'),
('Lia Susanti', 'Jl. Palangkaraya No. 215', '089567890123', 'lia@example.com'),
('Rian Prasetyo', 'Jl. Banjarbaru No. 220', '089678901234', 'rian@example.com'),
('Ani Puspita', 'Jl. Balikpapan No. 225', '089789012345', 'ani@example.com'),
('Arif Purnomo', 'Jl. Ternate No. 230', '089890123456', 'arif@example.com'),
('Dian Setiawan', 'Jl. Tidore No. 235', '089901234567', 'dian@example.com'),
('Rina Susanto', 'Jl. Maluku No. 240', '089012345678', 'rina_s@example.com'),
('Andi Saputra', 'Jl. Ambon No. 245', '089123456789', 'andi_s@example.com'),
('Nurul Hidayah', 'Jl. Papua No. 250', '089234567890', 'nurul@example.com'),
('Rizal Pratama', 'Jl. Sorong No. 255', '089345678901', 'rizal@example.com'),
('Rini Rahayu', 'Jl. Nabire No. 260', '089456789012', 'rini_r@example.com');

SET citus.shard_replication_factor = 2;

CREATE TABLE Kendaraan (
    ID_Kendaraan SERIAL PRIMARY KEY,
    Jenis_Kendaraan VARCHAR(50),
    Merek VARCHAR(50),
    Tahun_Produksi INT,
    Nomor_Plat VARCHAR(20)
);

INSERT INTO Kendaraan (Jenis_Kendaraan, Merek, Tahun_Produksi, Nomor_Plat)
VALUES
    ('Mobil', 'Toyota', 2018, 'AB 1234 CD'),
    ('Motor', 'Honda', 2020, 'B 5678 EF'),
    ('Truk', 'Isuzu', 2015, 'D 9876 HG'),
    ('Mobil', 'Nissan', 2019, 'F 5432 IJ'),
    ('Motor', 'Yamaha', 2021, 'K 3210 LM'),
    ('SUV', 'Mitsubishi', 2017, 'N 6789 OP'),
    ('Mobil', 'Ford', 2016, 'Q 2468 RS'),
    ('Motor', 'Suzuki', 2022, 'T 1357 UV'),
    ('Truk', 'Hino', 2014, 'W 8765 XY'),
    ('Mobil', 'Chevrolet', 2020, 'Z 4321 ZA'),
    ('Motor', 'Kawasaki', 2019, 'AA 9876 BC'),
    ('SUV', 'Jeep', 2018, 'BD 6543 EF'),
    ('Mobil', 'BMW', 2017, 'FG 1098 HI'),
    ('Motor', 'Ducati', 2021, 'JK 7654 LM'),
    ('Truk', 'Volvo', 2016, 'MN 3210 OP'),
    ('Mobil', 'Mercedes-Benz', 2015, 'QR 5432 ST'),
    ('Motor', 'Harley-Davidson', 2020, 'UV 8765 WX'),
    ('SUV', 'Land Rover', 2019, 'YZ 2109 AB'),
    ('Mobil', 'Audi', 2018, 'CD 6789 DE'),
    ('Motor', 'Triumph', 2022, 'EF 5432 GH'),
    ('Truk', 'Scania', 2017, 'IJ 8765 KL'),
    ('Mobil', 'Hyundai', 2016, 'LM 4321 MN'),
    ('Motor', 'Aprilia', 2021, 'OP 1098 QR'),
    ('SUV', 'Subaru', 2020, 'ST 7654 UV'),
    ('Mobil', 'Volkswagen', 2019, 'WX 3210 YZ'),
    ('Motor', 'Piaggio', 2018, 'AB 6543 CD'),
    ('Truk', 'Renault', 2015, 'DE 9876 FG'),
    ('Mobil', 'Peugeot', 2021, 'HI 5432 IJ'),
    ('Motor', 'Moto Guzzi', 2016, 'KL 2109 MN'),
    ('SUV', 'Porsche', 2020, 'OP 6789 QR'),
    ('Mobil', 'Ferrari', 2019, 'ST 4321 UV'),
    ('Motor', 'Indian Motorcycle', 2018, 'WX 1098 YZ'),
    ('Truk', 'MAN', 2017, 'AB 7654 CD'),
    ('Mobil', 'Lamborghini', 2022, 'EF 3210 FG'),
    ('Motor', 'Bajaj', 2021, 'GH 6543 IJ'),
    ('SUV', 'Bentley', 2016, 'KL 9876 MN'),
    ('Mobil', 'Bugatti', 2015, 'OP 5432 QR'),
    ('Motor', 'Royal Enfield', 2020, 'ST 2109 UV'),
    ('Truk', 'Daf', 2019, 'WX 8765 YZ'),
    ('Mobil', 'Alfa Romeo', 2018, 'AB 3210 CD'),
    ('Motor', 'Cagiva', 2017, 'EF 6543 FG'),
    ('SUV', 'Hummer', 2021, 'GH 1098 IJ'),
    ('Mobil', 'Infiniti', 2016, 'KL 7654 MN'),
    ('Motor', 'Zero Motorcycles', 2020, 'OP 4321 QR'),
    ('Truk', 'Iveco', 2019, 'ST 9876 UV'),
    ('Mobil', 'Jaguar', 2018, 'WX 5432 YZ'),
    ('Motor', 'Mv Agusta', 2017, 'AB 2109 CD'),
    ('SUV', 'Tesla', 2022, 'EF 8765 FG'),
    ('Mobil', 'Rolls-Royce', 2021, 'GH 3210 IJ'),
    ('Motor', 'Victory Motorcycles', 2018, 'KL 6543 MN'),
    ('Truk', 'Kenworth', 2016, 'OP 1098 QR'),
    ('Mobil', 'Maserati', 2015, 'ST 7654 UV'),
    ('Motor', 'Norton Motorcycle', 2020, 'WX 4321 YZ'),
    ('SUV', 'Cadillac', 2019, 'AB 9876 CD'),
    ('Mobil', 'McLaren', 2018, 'EF 5432 FG'),
    ('Motor', 'MV Agusta', 2017, 'GH 2109 IJ'),
    ('SUV', 'Aston Martin', 2021, 'KL 8765 MN');

CREATE TABLE Penyewaan_Kendaraan (
    ID_Penyewaan SERIAL PRIMARY KEY,
    ID_Pelanggan INT,
    ID_Kendaraan INT,
    Tanggal_Penyewaan DATE,
    Tanggal_Pengembalian DATE,
    Total_Biaya DECIMAL(10,2)
);

INSERT INTO Penyewaan_Kendaraan (ID_Pelanggan, ID_Kendaraan, Tanggal_Penyewaan, Tanggal_Pengembalian, Total_Biaya) 
VALUES
(1, 1, '2024-03-01', '2024-03-05', 1500000),
(2, 2, '2024-03-02', '2024-03-07', 2000000),
(3, 3, '2024-03-03', '2024-03-06', 1000000),
(4, 4, '2024-03-04', '2024-03-08', 1800000),
(5, 5, '2024-03-05', '2024-03-09', 1700000),
(6, 6, '2024-03-06', '2024-03-10', 1200000),
(7, 7, '2024-03-07', '2024-03-11', 1600000),
(8, 8, '2024-03-08', '2024-03-12', 1900000),
(9, 9, '2024-03-09', '2024-03-13', 1300000),
(10, 10, '2024-03-10', '2024-03-14', 2200000),
(1, 1, '2024-03-01', '2024-03-05', 1500000),
(2, 2, '2024-03-02', '2024-03-07', 2000000),
(3, 3, '2024-03-03', '2024-03-06', 1000000),
(4, 4, '2024-03-04', '2024-03-08', 1800000),
(5, 5, '2024-03-05', '2024-03-09', 1700000),
(6, 6, '2024-03-06', '2024-03-10', 1200000),
(7, 7, '2024-03-07', '2024-03-11', 1600000),
(8, 8, '2024-03-08', '2024-03-12', 1900000),
(9, 9, '2024-03-09', '2024-03-13', 1300000),
(10, 10, '2024-03-10', '2024-03-14', 2200000),
(1, 1, '2024-03-01', '2024-03-05', 1500000),
(2, 2, '2024-03-02', '2024-03-07', 2000000),
(3, 3, '2024-03-03', '2024-03-06', 1000000),
(4, 4, '2024-03-04', '2024-03-08', 1800000),
(5, 5, '2024-03-05', '2024-03-09', 1700000),
(6, 6, '2024-03-06', '2024-03-10', 1200000),
(7, 7, '2024-03-07', '2024-03-11', 1600000),
(8, 8, '2024-03-08', '2024-03-12', 1900000),
(9, 9, '2024-03-09', '2024-03-13', 1300000),
(10, 10, '2024-03-10', '2024-03-14', 2200000),
(1, 1, '2024-03-01', '2024-03-05', 1500000),
(2, 2, '2024-03-02', '2024-03-07', 2000000),
(3, 3, '2024-03-03', '2024-03-06', 1000000),
(4, 4, '2024-03-04', '2024-03-08', 1800000),
(5, 5, '2024-03-05', '2024-03-09', 1700000),
(6, 6, '2024-03-06', '2024-03-10', 1200000),
(7, 7, '2024-03-07', '2024-03-11', 1600000),
(8, 8, '2024-03-08', '2024-03-12', 1900000),
(9, 9, '2024-03-09', '2024-03-13', 1300000),
(10, 10, '2024-03-10', '2024-03-14', 2200000);

CREATE TABLE Rating_Pelanggan (
    ID_Rating SERIAL PRIMARY KEY,
    ID_Penyewaan INT,
    Rating INT
);

CREATE TABLE Pembayaran (
    ID_Pembayaran SERIAL PRIMARY KEY,
    ID_Penyewaan INT,
    Metode_Pembayaran VARCHAR(50),
    Tanggal_Pembayaran DATE,
    Jumlah_Pembayaran DECIMAL(10,2)
);

INSERT INTO Pembayaran (ID_Penyewaan, Metode_Pembayaran, Tanggal_Pembayaran, Jumlah_Pembayaran) VALUES
(1, 'Transfer Bank', '2024-03-05', 1500000),
(2, 'Kartu Kredit', '2024-03-07', 2000000),
(3, 'Tunai', '2024-03-06', 1000000),
(4, 'Transfer Bank', '2024-03-08', 1800000),
(5, 'Kartu Debit', '2024-03-09', 1700000),
(6, 'Tunai', '2024-03-10', 1200000),
(7, 'Transfer Bank', '2024-03-11', 1600000),
(8, 'Kartu Kredit', '2024-03-12', 1900000),
(9, 'Transfer Bank', '2024-03-13', 1300000),
(10, 'Tunai', '2024-03-14', 2200000),
(11, 'Kartu Kredit', '2024-03-15', 1850000),
(12, 'Transfer Bank', '2024-03-16', 1400000),
(13, 'Tunai', '2024-03-17', 1650000),
(14, 'Kartu Debit', '2024-03-18', 1950000),
(15, 'Transfer Bank', '2024-03-19', 1250000),
(16, 'Kartu Kredit', '2024-03-20', 2100000),
(17, 'Tunai', '2024-03-21', 1350000),
(18, 'Transfer Bank', '2024-03-22', 1550000),
(19, 'Kartu Kredit', '2024-03-23', 1700000),
(20, 'Tunai', '2024-03-24', 2000000),
(21, 'Transfer Bank', '2024-03-25', 1450000),
(22, 'Kartu Debit', '2024-03-26', 1800000),
(23, 'Tunai', '2024-03-27', 1900000),
(24, 'Transfer Bank', '2024-03-28', 2050000),
(25, 'Kartu Kredit', '2024-03-29', 1600000),
(26, 'Tunai', '2024-03-30', 1750000),
(27, 'Transfer Bank', '2024-03-31', 1300000),
(28, 'Kartu Debit', '2024-04-01', 2150000),
(29, 'Tunai', '2024-04-02', 1500000),
(30, 'Transfer Bank', '2024-04-03', 1850000),
(31, 'Kartu Kredit', '2024-04-04', 1200000),
(32, 'Tunai', '2024-04-05', 1950000),
(33, 'Transfer Bank', '2024-04-06', 1750000),
(34, 'Kartu Kredit', '2024-04-07', 1300000),
(35, 'Tunai', '2024-04-08', 1650000),
(36, 'Kartu Debit', '2024-04-09', 2050000),
(37, 'Transfer Bank', '2024-04-10', 1400000),
(38, 'Tunai', '2024-04-11', 2000000),
(39, 'Kartu Kredit', '2024-04-12', 1500000),
(40, 'Transfer Bank', '2024-04-13', 1700000),
(41, 'Tunai', '2024-04-14', 1900000),
(42, 'Kartu Kredit', '2024-04-15', 1250000),
(43, 'Transfer Bank', '2024-04-16', 2100000),
(44, 'Kartu Debit', '2024-04-17', 1350000),
(45, 'Tunai', '2024-04-18', 1550000),
(46, 'Kartu Kredit', '2024-04-19', 2000000),
(47, 'Transfer Bank', '2024-04-20', 1450000),
(48, 'Tunai', '2024-04-21', 1800000),
(49, 'Kartu Debit', '2024-04-22', 2050000),
(50, 'Transfer Bank', '2024-04-23', 1600000),
(51, 'Tunai', '2024-04-24', 1750000),
(52, 'Kartu Kredit', '2024-04-25', 1300000),
(53, 'Transfer Bank', '2024-04-26', 1900000),
(54, 'Kartu Debit', '2024-04-27', 1400000),
(55, 'Tunai', '2024-04-28', 1950000),
(56, 'Kartu Kredit', '2024-04-29', 1500000),
(57, 'Transfer Bank', '2024-04-30', 1850000),
(58, 'Tunai', '2024-05-01', 1700000),
(59, 'Kartu Debit', '2024-05-02', 2000000),
(60, 'Transfer Bank', '2024-05-03', 1550000);

SELECT undistribute_table('rating_pelanggan');
SELECT undistribute_table('penyewaan_kendaraan');
SELECT undistribute_table('pembayaran');
SELECT undistribute_table('pelanggan');
SELECT undistribute_table('kendaraan');

SELECT * FROM citus_tables;
select * from citus_shards;

SELECT * FROM kendaraan_102264;
SELECT * FROM penyewaan_kendaraan_102232;
SELECT * FROM pembayaran_102170;
SELECT * FROM rating_pelanggan_102204;
SELECT * FROM pelanggan_102296;