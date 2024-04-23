# Data Structure & Algorithm
- Struktur Data adalah suatu jalan untuk mengorganisasi dan mengelompokkan data agar data tersebut bisa diakses dan berguna dengan efisien. Struktur Data mendefinisikan hubungan antara data dan operasi yang bisa dilakukan dalam data. 

## Kenapa harus membutuhkan Stuktur Data?
    1. Pengorganisasian: Stuktur Data sangat membantu merapikan data dengan mudah dicari dan digunakan.
    2. Efisien: Membuat program menjadi lebih cepat karena menggunakan Struktur Data untuk dengan cepat menemukan dan memanipulasi data.
    3. Penyelesaian Masalah: Pada suatu pekerjaan yang kompleks, struktur data seperti kepingan puzzle yang membantu pengguna menyelesaikan masalah besar langkah demi langkah.
    4. Tidak Menghabiskan Banyak Ruang: Membantu penggunaan memori komputer sedikit, dan mengurangi error.
    5. Menjadi Kode tetap Rapi: Membuat kdoe terorganisir dan dengan mudah dibaca dan dimengerti.
    6. Bekerja Bersama: Beberapa Struktur Data sangat bagus untuk pekerjaan yang berbeda, jadi pengguna menggunakan ini untuk memperoleh hasil yang benar.

# List, Tuple, Dictionary & Set
**1. List:**
     List adalah struktur data yang dapat menyimpan beberapa elemen dalam urutan tertentu. List bersifat mutable, artinya elemen-elemen di dalamnya dapat diubah setelah list dibuat.

   - **Method dan Contoh Penggunaannya:**
     - `append()`: Menambahkan elemen ke akhir list.
       ```python
       my_list = [1, 2, 3]
       my_list.append(4)
       ```

     - `extend()`: Menambahkan elemen dari iterable ke akhir list.
       ```python
       my_list = [1, 2, 3]
       my_list.extend([4, 5, 6])
       ```

     - `insert()`: Menyisipkan elemen pada indeks tertentu.
       ```python
       my_list = [1, 2, 3]
       my_list.insert(1, 4)
       ```

     - `remove()`: Menghapus elemen tertentu dari list.
       ```python
       my_list = [1, 2, 3]
       my_list.remove(2)
       ```

**2. Tuple:**
     Tuple mirip dengan list, tetapi bersifat immutable, artinya setelah tuple dibuat, elemen-elemen di dalamnya tidak dapat diubah.

   - **Method dan Contoh Penggunaannya:**
     - `count()`: Menghitung jumlah kemunculan suatu elemen.
       ```python
       my_tuple = (1, 2, 2, 3)
       count_two = my_tuple.count(2)
       ```

     - `index()`: Mendapatkan indeks pertama kali munculnya suatu elemen.
       ```python
       my_tuple = (1, 2, 3, 4)
       index_three = my_tuple.index(3)
       ```

**3. Dictionary:**
     Dictionary adalah struktur data yang menyimpan data dalam bentuk pasangan key-value. Setiap key harus unik.

   - **Method dan Contoh Penggunaannya:**
     - `get()`: Mendapatkan nilai berdasarkan key.
       ```python
       my_dict = {'name': 'John', 'age': 25}
       age = my_dict.get('age')
       ```

     - `keys()`: Mengembalikan semua keys dalam dictionary.
       ```python
       my_dict = {'name': 'John', 'age': 25}
       all_keys = my_dict.keys()
       ```

     - `values()`: Mengembalikan semua values dalam dictionary.
       ```python
       my_dict = {'name': 'John', 'age': 25}
       all_values = my_dict.values()
       ```

**4. Set:**
     Set adalah struktur data yang tidak memiliki indeks dan tidak mengizinkan elemen yang sama. Set bersifat mutable.

   - **Method dan Contoh Penggunaannya:**
     - `add()`: Menambahkan elemen ke dalam set.
       ```python
       my_set = {1, 2, 3}
       my_set.add(4)
       ```

     - `remove()`: Menghapus elemen tertentu dari set.
       ```python
       my_set = {1, 2, 3}
       my_set.remove(2)
       ```

     - `union()`: Menggabungkan dua set.
       ```python
       set1 = {1, 2, 3}
       set2 = {3, 4, 5}
       union_set = set1.union(set2)
       ```

# Searching & Sorting
**1. Searching:**
     Searching (pencarian) adalah proses menemukan posisi atau keberadaan elemen tertentu dalam suatu struktur data. Beberapa metode pencarian umum melibatkan algoritma yang dapat digunakan untuk menemukan elemen yang dicari.

   - **Metode Pencarian:**
     - **Linear Search (Pencarian Linear):** Mencari elemen satu per satu hingga elemen yang dicari ditemukan atau mencapai akhir struktur data.

       ```python
       def linear_search(arr, target):
           for i in range(len(arr)):
               if arr[i] == target:
                   return i
           return -1
       ```

     - **Binary Search (Pencarian Biner):** Hanya dapat digunakan pada data yang sudah diurutkan. Membandingkan elemen tengah dengan elemen yang dicari dan mengurangi rentang pencarian setiap iterasi.

       ```python
       def binary_search(arr, target):
           low, high = 0, len(arr) - 1
           while low <= high:
               mid = (low + high) // 2
               if arr[mid] == target:
                   return mid
               elif arr[mid] < target:
                   low = mid + 1
               else:
                   high = mid - 1
           return -1
       ```

**2. Sorting:**
     Sorting (pengurutan) adalah proses menyusun elemen-elemen suatu struktur data dalam urutan tertentu. Pengurutan dapat dilakukan dengan berbagai algoritma, dan pilihan algoritma bergantung pada kebutuhan dan karakteristik data.

   - **Metode Pengurutan:**
     - **Bubble Sort:** Membandingkan dan menukar elemen secara berpasangan hingga seluruh data terurut.

       ```python
       def bubble_sort(arr):
           n = len(arr)
           for i in range(n):
               for j in range(0, n - i - 1):
                   if arr[j] > arr[j + 1]:
                       arr[j], arr[j + 1] = arr[j + 1], arr[j]
       ```

     - **Quick Sort:** Memilih elemen "pivot" dan mempartisi array menjadi dua bagian: elemen yang lebih kecil dari pivot dan elemen yang lebih besar dari pivot. Proses ini diulang pada setiap bagian.

       ```python
       def quick_sort(arr):
           if len(arr) <= 1:
               return arr
           else:
               pivot = arr[0]
               less = [x for x in arr[1:] if x <= pivot]
               greater = [x for x in arr[1:] if x > pivot]
               return quick_sort(less) + [pivot] + quick_sort(greater)
       ```

     - **Merge Sort:** Memisahkan array menjadi dua bagian, mengurutkan masing-masing bagian, dan menggabungkannya kembali.

       ```python
       def merge_sort(arr):
           if len(arr) <= 1:
               return arr
           mid = len(arr) // 2
           left = merge_sort(arr[:mid])
           right = merge_sort(arr[mid:])
           return merge(left, right)

       def merge(left, right):
           result = []
           i = j = 0
           while i < len(left) and j < len(right):
               if left[i] < right[j]:
                   result.append(left[i])
                   i += 1
               else:
                   result.append(right[j])
                   j += 1
           result.extend(left[i:])
           result.extend(right[j:])
           return result
       ```