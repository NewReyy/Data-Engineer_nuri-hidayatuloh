Relational Database

1. Pengenalan Database
- Database merupakan sekumpulan data yang terorganisir.
- Seperti contoh pada akun tweeter seseorang terdapat Username, email, nama lengkap, deskripsi, negara dan tanggal bergabung.

2. Relationship Database
- One to One, contohnya yakni 1 user hanya memiliki 1 foto profil
- One to Many, contohnya yakni 1 user bisa memiliki banyak tweets
- Many to Many, contohnya yakni 1 user bisa memiliki banyak followers user, 1 user bisa di follow banyak user. Selain itu, 1 mahasiswa bisa memiliki banyak matakuliah, 1 matakuliah bisa diambil oleh banyak mahasiswa.

* Bagaimana cara mengimplementasikannya?
- RDBMS (Relational Database Management Systems) software yang bisa digunakan sebagai dasarnya antara lain: MySQL.
3. Entity Relationship Diagram
Diagram Relasi Entitas (ERD) adalah representasi visual dari struktur dan hubungan antara entitas dalam sebuah basis data. Ini digunakan untuk merancang dan memodelkan hubungan antara entitas dalam suatu sistem informasi. Diagram ini menggunakan bentuk geometris seperti kotak untuk merepresentasikan entitas dan garis untuk merepresentasikan hubungan antara entitas. Berikut adalah contoh sederhana penjelasan ERD:

Misalkan dimiliki sebuah sistem perpustakaan dengan entitas utama berikut:
1. Buku
2. Penulis
3. Peminjam

Berikut adalah contoh ERD untuk sistem perpustakaan:

```
     +-------------+     1       M      +-------------+
     |   Penulis   | -----------------  |    Buku     |
     +-------------+                    +-------------+
     | Penulis_ID  | <--------------->  |   Buku_ID   |
     |   Nama      |                    |    Judul    |
     |   Alamat    |                    |  Penulis_ID |
     +-------------+                    +-------------+
            |                                    |
            | 1                                M |
            |                                    |
            |                                    |
            |                                    |
            v                                    v
     +-------------+                    +-------------+
     |  Peminjam   |                    |    Pinjam   |
     +-------------+                    +-------------+
     | Peminjam_ID | <--------------->  |  Pinjam_ID  |
     |   Nama      |                    |   Buku_ID   |
     |   Alamat    |                    |  PeminjamID |
     +-------------+                    +-------------+
```

Penjelasan ERD di atas:
- Setiap buku memiliki satu penulis, tetapi satu penulis dapat menulis banyak buku. Ini adalah hubungan "One-to-Many" antara entitas Penulis dan Buku.
- Setiap buku dapat dipinjam oleh banyak peminjam, dan setiap peminjam dapat meminjam banyak buku. Ini adalah hubungan "Many-to-Many" antara entitas Buku dan Peminjam, yang diimplementasikan melalui entitas Pinjam yang menghubungkan kedua entitas tersebut.
- Setiap peminjam dapat memiliki satu atau lebih buku yang dipinjam, tetapi setiap buku hanya dapat dipinjam oleh satu peminjam pada suatu waktu tertentu.

4. SQL Statement
Tiga sub-bahasa utama dalam SQL (Structured Query Language) adalah DDL (Data Definition Language), DML (Data Manipulation Language), dan DCL (Data Control Language). Ini adalah bagian-bagian utama yang membentuk dasar bahasa SQL dan digunakan untuk berinteraksi dengan basis data. Berikut penjelasan dan contoh dari masing-masing sub-bahasa:

### 1. DDL (Data Definition Language):
DDL digunakan untuk mendefinisikan struktur atau skema dari basis data. Ini mencakup operasi seperti membuat, mengubah, dan menghapus objek dalam basis data.

Contoh operasi DDL termasuk:
- CREATE: Untuk membuat objek baru seperti tabel, indeks, atau tampilan.
- ALTER: Untuk mengubah struktur objek yang sudah ada, misalnya menambahkan kolom ke tabel.
- DROP: Untuk menghapus objek dari basis data, seperti menghapus tabel atau indeks.

Contoh:
```sql
CREATE TABLE Employees (
    ID INT PRIMARY KEY,
    Name VARCHAR(50),
    Department VARCHAR(50)
);

ALTER TABLE Employees
ADD COLUMN Salary DECIMAL(10, 2);

DROP TABLE Employees;
```

Di MySQL, terdapat beberapa tipe data yang umum digunakan untuk menyimpan berbagai jenis nilai. Berikut adalah tiga tipe data umum yang sering digunakan:

#### 1. Numerik (Num):
Tipe data numerik digunakan untuk menyimpan nilai numerik seperti angka bulat atau desimal. Beberapa contoh tipe data numerik di MySQL termasuk:
- INT: Untuk menyimpan nilai bilangan bulat.
- FLOAT: Untuk menyimpan nilai desimal dengan presisi floating point.
- DOUBLE: Untuk menyimpan nilai desimal dengan presisi double-precision.
- DECIMAL: Untuk menyimpan nilai desimal yang mempertahankan presisi yang tepat.

Contoh:
```sql
CREATE TABLE Products (
    ProductID INT,
    Price DECIMAL(10, 2),
    Quantity INT
);
```

#### 2. Karakter (Huruf):
Tipe data karakter digunakan untuk menyimpan data dalam bentuk teks atau karakter. Beberapa contoh tipe data karakter di MySQL termasuk:
- CHAR: Untuk menyimpan string dengan panjang tetap.
- VARCHAR: Untuk menyimpan string dengan panjang variabel.
- TEXT: Untuk menyimpan string teks panjang.

Contoh:
```sql
CREATE TABLE Employees (
    Name VARCHAR(50),
    Address TEXT
);
```

#### 3. Tanggal (Date):
Tipe data tanggal digunakan untuk menyimpan nilai tanggal dan waktu. Beberapa contoh tipe data tanggal di MySQL termasuk:
- DATE: Untuk menyimpan nilai tanggal.
- DATETIME: Untuk menyimpan nilai tanggal dan waktu.
- TIMESTAMP: Untuk menyimpan nilai tanggal dan waktu dalam format terstandarisasi.

Contoh:
```sql
CREATE TABLE Orders (
    OrderID INT,
    OrderDate DATE,
    ShipDate DATETIME
);
```

### 2. DML (Data Manipulation Language):
DML digunakan untuk mengelola data dalam basis data. Ini mencakup operasi seperti menambah, mengubah, menghapus, dan memperoleh data dari tabel.

Contoh operasi DML termasuk:
- INSERT: Untuk menambahkan data baru ke dalam tabel.
- UPDATE: Untuk mengubah data yang sudah ada dalam tabel.
- DELETE: Untuk menghapus data dari tabel.
- SELECT: Untuk memperoleh data dari tabel.

Contoh:
```sql
INSERT INTO Employees (ID, Name, Department, Salary)
VALUES (1, 'John Doe', 'IT', 50000.00);

UPDATE Employees
SET Salary = 55000.00
WHERE ID = 1;

DELETE FROM Employees
WHERE ID = 1;

SELECT * FROM Employees;
```

Berikut adalah penjelasan singkat dan contoh penggunaan dari berbagai pernyataan DML (Data Manipulation Language) dalam SQL:

#### 1. LIKE:
Digunakan untuk mencocokkan pola dalam kolom data.

Contoh:
```sql
SELECT * FROM Employees WHERE Name LIKE 'J%';
```

#### 2. BETWEEN:
Digunakan untuk memilih nilai di antara dua nilai tertentu.

Contoh:
```sql
SELECT * FROM Products WHERE Price BETWEEN 10 AND 50;
```

#### 3. AND, OR:
Digunakan untuk menggabungkan beberapa kondisi dalam klausa WHERE.

Contoh:
```sql
SELECT * FROM Employees WHERE Age > 25 AND Department = 'IT';
```

#### 4. ORDER BY:
Digunakan untuk mengurutkan hasil query berdasarkan satu atau lebih kolom.

Contoh:
```sql
SELECT * FROM Products ORDER BY Price DESC;
```

#### 5. LIMIT:
Digunakan untuk membatasi jumlah baris yang dikembalikan oleh sebuah query.

Contoh:
```sql
SELECT * FROM Customers LIMIT 10;
```

#### 6. JOIN (INNER, LEFT, RIGHT):
Digunakan untuk menggabungkan baris dari dua atau lebih tabel berdasarkan kondisi tertentu.

Contoh:
```sql
SELECT Orders.OrderID, Customers.CustomerName
FROM Orders
INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID;
```

#### 7. UNION:
Digunakan untuk menggabungkan hasil dari dua atau lebih pernyataan SELECT.

Contoh:
```sql
SELECT City FROM Customers
UNION
SELECT City FROM Suppliers;
```

#### 8. Agregat (MIN, MAX, SUM, AVG, COUNT, HAVING):
Digunakan untuk melakukan operasi agregat pada grup data.

Contoh:
```sql
SELECT Department, AVG(Salary) AS AverageSalary
FROM Employees
GROUP BY Department
HAVING AVG(Salary) > 50000;
```

#### 9. Subquery:
Query yang tertanam di dalam query utama.

Contoh:
```sql
SELECT Name, Department
FROM Employees
WHERE Salary > (SELECT AVG(Salary) FROM Employees);
```

#### 10. Function (Stored Procedure, View, Trigger):
- Stored Procedure: Serangkaian pernyataan SQL yang disimpan di database untuk penggunaan berulang.
- View: Sebuah query yang disimpan sebagai objek di database.
- Trigger: Sebuah tindakan yang dilakukan secara otomatis saat suatu peristiwa tertentu terjadi pada tabel.

Contoh:
```sql
CREATE VIEW HighSalaryEmployees AS
SELECT * FROM Employees WHERE Salary > 70000;
```

```sql
CREATE TRIGGER AfterInsertOrder
AFTER INSERT ON Orders
FOR EACH ROW
BEGIN
    INSERT INTO OrderLogs (OrderID, Action) VALUES (NEW.OrderID, 'Inserted');
END;
```

### 3. DCL (Data Control Language):
DCL digunakan untuk mengontrol hak akses dan izin pada objek-objek dalam basis data.

Contoh operasi DCL termasuk:
- GRANT: Untuk memberikan hak akses tertentu kepada pengguna pada objek dalam basis data.
- REVOKE: Untuk mencabut hak akses yang telah diberikan sebelumnya.

Contoh:
```sql
GRANT SELECT, INSERT, UPDATE ON Employees TO user1;

REVOKE INSERT ON Employees FROM user1;
```