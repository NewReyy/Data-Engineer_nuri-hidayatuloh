### Resume

Basic Programming with Python:

- **Apa itu Python**: Python adalag salah satu bahasa pemrograman, yang bisa dikategorikan dalam High-Level atau tingkat tinggi. Python tidak memerlukan kompilasi seperti bahasa pemrograman lainnya atau bisa disebut (Interpretasi) agar bisa lebih cepat dan fleksibel.
- **Variable & Type Data di Python**: Variable digunakan untuk menyimpan informasi dalam program komputer, menyediakan cara memberi label data dengan nama deskriptif dan memiliki tipe data (boolean, numerik, string).
1. **Numeric**: 
    * Integer, merupakan variabel yang mendefinisikan nilai yang bersifat bilangan atau angka. Seperti contoh : 1, 2, 3, 98. 
    * Float, merupakan variabel yang mendefinisikan nilai yang bersifat bilangan desimal atau yang memiliki koma setelahnya. Seperti contoh : 3.14, 98.34
    * Complex, variabel ini digunakan untuk merepresentasikan bilangan kompleks. Bilangan kompleks memiliki dua bagian: bagian real (real part) dan bagian imajiner (imaginary part), yang ditulis dalam bentuk a + bj, di mana a adalah bagian real, b adalah bagian imajiner, dan j adalah unit imajiner (yang merupakan akar kuadrat dari -1).
    ```python
    bilangan_kompleks1 = 3 + 4j
    bilangan_kompleks2 = 1 - 2j
    ```
2. **Dictionary**: merupakan variabel yang digunakan untuk menyimpan pasangan kunci-nilai(key-value). Setiap kunci bersifat unik, variabel ini didefinisikan dengan tanda kurung kurawal '{}', dengan format 'kunci: nilai'.
    ```python
    my_dict = {'nama': 'John', 'umur': 25, 'kota': 'Jakarta'}
    ```

3. **Boolean**: merupakan varibel yang hanya mempunyai nilai yakni True or False atau bisa juga 0 bernilai False dan 1 bernilai True.
4. **Set**:  Set atau Himpunan merupakan variabel yang digunakan untuk menyimpan himpunan elemen tanpa urutan tertentu dan isian dari Set tidak boleh lebih dari satu kali. Set didefinisikan dengan tanda kurung kurawal juga sama seperti Dictionary namun bedanya, Set tidak mempunyai Key & Value seperti Dictionary.
    ```python
    my_set = {1, 2, 3, 'a', 'b', 'c'}
    ```
5. **Sequence Type**: 
    * String, merupakan variabel yang mendefinisikan nilai yang berupa karakter atau huruf. Dan isi dari variabel ini pasti ditandai dengan tanda baca petik dua ("")Seperti contoh : "Alterra", "Materinya", "Bagus"
    * List, merupakan variabel yang digunakan untuk menyimpan sejumlah elemen/data dalam daftar dan dapat diubah (mutable), artinya didalam variabel ini bisa menambah menghapus, atau mengubah nilai elemen-elemen tersebut. Variabel ini didefinisikan dengan menggunakan kurung siku '[]'
    ```python
    my_list = [1, 2, 3, 'a', 'b', 'c']
    ```
    * Tuple, merupakan variabel yang mirip dengan List, namun bersifat (immutable) atau tidak dapat diubah setelah tuple dibuat. Variabel ini didefinisikan dengan menggunakan kurung biasa '()'
    ```python
    my_tuple = (1, 2, 3, 'a', 'b', 'c')
    ```

- **Ekspresi pada Python**:  ekspresi adalah kombinasi dari nilai, variabel, operator, dan pemanggilan fungsi yang dievaluasi untuk menghasilkan nilai tunggal. Ekspresi bisa menjadi sangat sederhana atau kompleks tergantung pada bagaimana elemen-elemen tersebut dikombinasikan. Seperti contoh :
    ```python
    a = 5
    b = 3
    c = a + b  # Ekspresi ini mengevaluasi hasil penjumlahan a dan b
    ```
**Operator dalam Python:**
Operator dalam Python digunakan untuk melakukan operasi pada variabel dan nilai. Contoh operator termasuk operator aritmatika (+, -, *, /), operator perbandingan (==, !=, <, >), dan operator logika (and, or, not).

Contoh penggunaan operator:

```python
a = 5
b = 3

# Operator aritmatika
c = a + b
d = a * b

# Operator perbandingan
is_equal = a == b
is_greater = a > b

# Operator logika
logical_result = (a > 0) and (b < 10)
```

**Percabangan (Branching) dan Perulangan (Looping) dalam Python:**
Percabangan digunakan untuk membuat keputusan berdasarkan kondisi, sedangkan perulangan digunakan untuk mengulangi blok kode.

Contoh percabangan (if-else):

```python
nilai = 75

if nilai >= 70:
    print("Lulus")
else:
    print("Tidak Lulus")
```

Contoh perulangan (for loop):

```python
for i in range(5):
    print(i)
```

**Fungsi (Function) dalam Python:**
Fungsi digunakan untuk mengorganisir dan memecah program menjadi bagian-bagian yang lebih kecil, dapat digunakan kembali. Fungsi didefinisikan dengan kata kunci `def`.

Contoh fungsi:

```python
def tambah(a, b):
    return a + b

hasil_penjumlahan = tambah(3, 4)
print(hasil_penjumlahan)
```

**Waktu dan Kompleksitas Ruang (Time and Space Complexity) dalam Python:**
Waktu kompleksitas dan kompleksitas ruang mengukur kinerja dan penggunaan memori dari sebuah algoritma. Dinyatakan dengan notasi O().

Contoh:

```python
# Waktu kompleksitas O(n)
def linear_search(arr, target):
    for element in arr:
        if element == target:
            return True
    return False
```

**Tipe Data String dalam Python:**
String adalah tipe data yang digunakan untuk menyimpan teks. String didefinisikan dengan tanda kutip (bisa tunggal atau ganda).

Contoh string:

```python
nama = "John"
kalimat = 'Halo, apa kabar?'
```

**Manipulasi String dalam Python:**
Manipulasi string mencakup berbagai operasi, seperti penggabungan, pemotongan, dan transformasi string.

Contoh manipulasi string:

```python
sapaan = "Halo"
nama = "John"
kalimat = sapaan + " " + nama  # Penggabungan string
potongan_nama = nama[0:3]  # Pemotongan string
uppercase_nama = nama.upper()  # Transformasi ke huruf besar
```