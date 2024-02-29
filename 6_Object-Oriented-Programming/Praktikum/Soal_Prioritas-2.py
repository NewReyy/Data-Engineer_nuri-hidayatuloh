# Kelas Pelanggan
class Pelanggan:
    def __init__(self, nama, usia, id_pelanggan):
        self.__nama = nama
        self.__usia = usia
        self.__id_pelanggan = id_pelanggan

    def get_nama(self):
        return self.__nama

    def set_nama(self, nama):
        self.__nama = nama

    def get_usia(self):
        return self.__usia

    def set_usia(self, usia):
        self.__usia = usia

    def get_id_pelanggan(self):
        return self.__id_pelanggan

    def set_id_pelanggan(self, id_pelanggan):
        self.__id_pelanggan = id_pelanggan

    def tampilkanInfo(self):
        print(f"ID Pelanggan: {self.__id_pelanggan}")
        print(f"Nama: {self.__nama}")
        print(f"Usia: {self.__usia} tahun")


# Kelas Pelatih
class Pelatih:
    def __init__(self, nama, spesialisasi, tahun_pengalaman):
        self.__nama = nama
        self.__spesialisasi = spesialisasi
        self.__tahun_pengalaman = tahun_pengalaman

    def get_nama(self):
        return self.__nama

    def set_nama(self, nama):
        self.__nama = nama

    def get_spesialisasi(self):
        return self.__spesialisasi

    def set_spesialisasi(self, spesialisasi):
        if spesialisasi.lower() in ["yoga", "angkatbeban"]:
            self.__spesialisasi = spesialisasi.lower()
        else:
            print("Spesialisasi tidak valid.")

    def get_tahun_pengalaman(self):
        return self.__tahun_pengalaman

    def set_tahun_pengalaman(self, tahun_pengalaman):
        self.__tahun_pengalaman = tahun_pengalaman

    def tampilkanInfo(self):
        print(f"Nama Pelatih: {self.__nama}")
        print(f"Spesialisasi: {self.__spesialisasi.capitalize()}")
        print(f"Tahun Pengalaman: {self.__tahun_pengalaman} tahun")


# Kelas KelasLatihan hanya mempunyai parameter jenis_latihan dan jadwal
class KelasLatihan(Pelatih):
    def __init__(self, jenis_latihan, jadwal):
        super().__init__("Placeholder", "Placeholder", 0)  # Menyertakan nilai default
        self.__jenis_latihan = jenis_latihan
        self.__jadwal = jadwal

    def tampilkanInfo(self):
        print(f"Jenis Latihan: {self.__jenis_latihan}")
        print(f"Jadwal: {self.__jadwal}")

# Kelas Turunan Yoga
class Yoga(KelasLatihan):
    def __init__(self, jenis_latihan, jadwal, tingkat_kesulitan):
        super().__init__(jenis_latihan, jadwal)
        self.__tingkat_kesulitan = tingkat_kesulitan

    def atur_posisi_yoga(self):
        print("Menyesuaikan posisi Yoga sesuai tingkat kesulitan.")


    def tampilkanInfo(self):
        super().tampilkanInfo()
        print(f"Tingkat Kesulitan: {self.__tingkat_kesulitan}")

# Kelas Turunan AngkatBeban
class AngkatBeban(KelasLatihan):
    def __init__(self, jenis_latihan, jadwal, berat_maksimum):
        super().__init__(jenis_latihan, jadwal)
        self.__berat_maksimum = berat_maksimum

    def atur_berat_beban(self):
        print(f"Mengatur berat beban maksimum: {self.__berat_maksimum} kg")

    def tampilkanInfo(self):
        super().tampilkanInfo()
        print(f"Berat Maksimum: {self.__berat_maksimum} kg")


# Demonstrasi Polymorphism
def info_dan_metode_khusus(kelas_latihan):
    kelas_latihan.tampilkanInfo()

    # Memanggil metode khusus berdasarkan tipe kelas
    if isinstance(kelas_latihan, Yoga):
        kelas_latihan.atur_posisi_yoga()
    elif isinstance(kelas_latihan, AngkatBeban):
        kelas_latihan.atur_berat_beban()
    else:
        print("Kelas latihan tidak dikenali.")


# Demonstrasi
yoga_kelas = Yoga("Yoga Pagi", "Senin", "Intermediate")
angkat_beban_kelas = AngkatBeban("AngkatBeban Sore", "Selasa", 50)

kelas_latihan_array = [yoga_kelas, angkat_beban_kelas]

# Menampilkan informasi dan metode khusus menggunakan polymorphism
for kelas_latihan in kelas_latihan_array:
    info_dan_metode_khusus(kelas_latihan)
    print("\n" + "=" * 30 + "\n")