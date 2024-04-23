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


# Demonstrasi
pelanggan1 = Pelanggan("Yazid Ahmad Hisyam", 20, "P001")
pelanggan2 = Pelanggan("Nimas Sekararum Kinanthi", 20, "P002")

pelatih1 = Pelatih("Coach Rayhan", "Yoga", 5)
pelatih2 = Pelatih("Coach Afril", "AngkatBeban", 8)

kelas_latihan1 = KelasLatihan("Yoga Pagi", "Senin, Rabu")
kelas_latihan2 = KelasLatihan("AngkatBeban Sore", "Selasa, Kamis")

print("Informasi Pelanggan:")
pelanggan1.tampilkanInfo()
print("\nInformasi Pelatih:")
pelatih1.tampilkanInfo()
print("\nInformasi Kelas Latihan 1:")
kelas_latihan1.tampilkanInfo()
print("\nInformasi Kelas Latihan 2:")
kelas_latihan2.tampilkanInfo()