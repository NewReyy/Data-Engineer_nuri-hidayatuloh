- **Object-Oriented Programming (OOP)** adalah paradigma pemrograman yang menggunakan konsep objek, di mana program dibangun dengan merinci objek yang mewakili entitas di dunia nyata.

- Membantu **mengorganisir dan merancang kode** dengan lebih terstruktur dan memungkinkan **penggunaan ulang kode** melalui konsep kelas dan objek.

- Diterapkan saat **mengembangkan aplikasi kompleks** yang memerlukan struktur yang jelas dan moduler.

- Cocok untuk pengembangan perangkat lunak yang melibatkan **manipulasi data kompleks atau interaksi antar komponen.**

- **Programmer atau pengembang perangkat lunak** yang ingin menggunakan pendekatan yang lebih terstruktur dalam pengkodean.

1. **Encapsulation (Pembungkus):**
   - **Definisi**: Mengikat data (variabel) dan metode (fungsi) yang bekerja pada data ke dalam satu unit tunggal, yaitu kelas.
   - **Contoh Penggunaan:**
     ```python
     class Animal:
         def __init__(self, name):
             self.name = name
             self.__age = 0  # Variabel private

         def get_age(self):
             return self.__age

         def increase_age(self):
             self.__age += 1

     cat = Animal("Whiskers")
     cat.increase_age()
     print(cat.get_age())  # Output: 1
     ```

2. **Data Abstraction (Abstraksi Data):**
   - **Definisi**: Menyembunyikan rincian implementasi dan hanya mengekspos fungsi-fungsi penting untuk penggunaan eksternal.
   - **Contoh Penggunaan:**
     ```python
     from abc import ABC, abstractmethod

     class Shape(ABC):
         @abstractmethod
         def area(self):
             pass

     class Circle(Shape):
         def __init__(self, radius):
             self.radius = radius

         def area(self):
             return 3.14 * self.radius * self.radius

     circle = Circle(5)
     print(circle.area())  # Output: 78.5
     ```

3. **Inheritance (Pewarisan):**
   - **Definisi**: Menggunakan kembali properti dan metode dari kelas yang sudah ada ke dalam kelas baru.
   - **Contoh Penggunaan:**
     ```python
     class Vehicle:
         def __init__(self, brand):
             self.brand = brand

     class Car(Vehicle):
         def __init__(self, brand, model):
             super().__init__(brand)
             self.model = model

     my_car = Car("Toyota", "Camry")
     print(my_car.brand)  # Output: Toyota
     ```

4. **Polymorphism (Polimorfisme):**
   - **Definisi**: Mengizinkan kelas atau objek menggunakan nama yang sama untuk melakukan tindakan yang berbeda.
   - **Contoh Penggunaan:**
     ```python
     class Dog:
         def sound(self):
             return "Bark"

     class Cat:
         def sound(self):
             return "Meow"

     def make_sound(animal):
         return animal.sound()

     dog = Dog()
     cat = Cat()

     print(make_sound(dog))  # Output: Bark
     print(make_sound(cat))  # Output: Meow
     ```

Dengan menggunakan konsep-konsep OOP ini, programmer dapat membuat kode yang lebih bersih, mudah dimengerti, dan mudah dipelihara. Ini juga memfasilitasi pengembangan perangkat lunak yang lebih skalabel dan modular.