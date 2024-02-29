# Membuat kelas Pelanggan
class Pelanggan:
    def __init__(self, nama, usia, id_pelanggan):
        self.__nama = nama
        self.__usia = usia
        self.__id_pelanggan = id_pelanggan

    def get_nama(self):
        return self.__nama

    def get_usia(self):
        return self.__usia

    def get_id_pelanggan(self):
        return self.__id_pelanggan

# Membuat kelas KelasLatihan
class KelasLatihan:
    def __init__(self, jenis_latihan, jadwal, kapasitas):
        self.__jenis_latihan = jenis_latihan
        self.__jadwal = jadwal
        self.__kapasitas = kapasitas
        self.__peserta_terdaftar = set()

    def tampilkanInfo(self):
        print(f"Jenis Latihan: {self.__jenis_latihan}")
        print(f"Jadwal: {self.__jadwal}")
        print(f"Kapasitas: {self.__kapasitas} orang")

    def pesanKelas(self, pelanggan):
        if len(self.__peserta_terdaftar) < self.__kapasitas:
            self.__peserta_terdaftar.add(pelanggan)
            print(f"{pelanggan.get_nama()} berhasil mendaftar kelas {self.__jenis_latihan}.")
        else:
            print(f"Kelas {self.__jenis_latihan} sudah penuh. {pelanggan.get_nama()} tidak dapat mendaftar.")

    def batalkanKelas(self, pelanggan):
        if pelanggan in self.__peserta_terdaftar:
            self.__peserta_terdaftar.remove(pelanggan)
            print(f"{pelanggan.get_nama()} berhasil membatalkan kelas {self.__jenis_latihan}.")
        else:
            print(f"{pelanggan.get_nama()} tidak terdaftar pada kelas {self.__jenis_latihan}.")


# Membuat kelas ManajemenPelanggan
class ManajemenPelanggan:
    def __init__(self):
        self.__daftar_pelanggan = []

    def registerPelanggan(self, nama, usia):
        id_pelanggan = f"P{len(self.__daftar_pelanggan) + 1:03d}"
        pelanggan_baru = Pelanggan(nama, usia, id_pelanggan)
        self.__daftar_pelanggan.append(pelanggan_baru)
        print(f"Registrasi berhasil. ID Pelanggan Anda: {id_pelanggan}")
        return pelanggan_baru

    def loginPelanggan(self, id_pelanggan):
        for pelanggan in self.__daftar_pelanggan:
            if pelanggan.get_id_pelanggan() == id_pelanggan:
                print(f"Selamat datang, {pelanggan.get_nama()}!")
                return pelanggan
        print("ID Pelanggan tidak ditemukan.")
        return None

# Fungsi utama Program
def main():
    manajemen_pelanggan = ManajemenPelanggan()
    yoga_kelas = KelasLatihan("Yoga Pagi", "Senin", 10)
    angkat_beban_kelas = KelasLatihan("AngkatBeban Sore", "Selasa", 8)

    pelanggan_terlogin = None

    while True:
        print("\n=== SISTEM PENDAFTARAN KELAS by Nuri Hidayatuloh DE Alterra Batch 6 ===")

        if pelanggan_terlogin:
            # Jika pelanggan sudah login, tampilkan menu khusus
            print("1. Kelas Terdaftar")
            print("2. Pesan Kelas")
            print("3. Batalkan Kelas")
            print("4. Keluar")
            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                # Informasi Kelas Terdaftar berdasarkan ID Pelanggan
                print("\nKelas yang terdaftar:")
                for peserta in yoga_kelas._KelasLatihan__peserta_terdaftar:
                    print(f"- {peserta.get_nama()} (Yoga Pagi)")
                for peserta in angkat_beban_kelas._KelasLatihan__peserta_terdaftar:
                    print(f"- {peserta.get_nama()} (AngkatBeban Sore)")

            elif pilihan == "2":
                # Pesan Kelas
                print("\nKelas yang tersedia:")
                print("1. Yoga Pagi")
                print("2. AngkatBeban Sore")
                print("Ketik Apapun untuk kembali ke Menu")
                kelas = input("Pilih kelas: ")

                if kelas == "1":
                    yoga_kelas.pesanKelas(pelanggan_terlogin)
                elif kelas == "2":
                    angkat_beban_kelas.pesanKelas(pelanggan_terlogin)
                else:
                    print("Kelas tidak valid.")

            elif pilihan == "3":
                # Batalkan Kelas
                print("\nKelas yang terdaftar:")
                for peserta in yoga_kelas._KelasLatihan__peserta_terdaftar:
                    print(f"- {peserta.get_nama()} (Yoga Pagi)")
                for peserta in angkat_beban_kelas._KelasLatihan__peserta_terdaftar:
                    print(f"- {peserta.get_nama()} (AngkatBeban Sore)")

                id_pelanggan = input("\nMasukkan ID Pelanggan yang akan membatalkan kelas: ")
                if id_pelanggan == pelanggan_terlogin.get_id_pelanggan():
                    yoga_kelas.batalkanKelas(pelanggan_terlogin)
                elif id_pelanggan == pelanggan_terlogin.get_id_pelanggan():
                    angkat_beban_kelas.batalkanKelas(pelanggan_terlogin)
                else:
                    print("ID Pelanggan tidak terdaftar pada kelas manapun.")

            elif pilihan == "4":
                # Keluar
                print("Terima kasih!")
                break

            else:
                print("Pilihan tidak valid. Silakan pilih kembali.")

        else:
            # Jika pelanggan belum login, tampilkan menu lengkap
            print("1. Register Pelanggan")
            print("2. Login Pelanggan")
            print("3. Keluar")
            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                nama = input("Masukkan nama: ")
                usia = int(input("Masukkan usia: "))
                manajemen_pelanggan.registerPelanggan(nama, usia)

            elif pilihan == "2":
                id_pelanggan = input("Masukkan ID Pelanggan: ")
                pelanggan_terlogin = manajemen_pelanggan.loginPelanggan(id_pelanggan)

            elif pilihan == "3":
                # Keluar
                print("Terima kasih!")
                break

            else:
                print("Pilihan tidak valid. Silakan pilih kembali.")


if __name__ == "__main__":
    main()