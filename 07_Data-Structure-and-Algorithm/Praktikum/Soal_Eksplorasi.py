import uuid
from getpass import getpass

class Pengguna:
    def __init__(self, nama_pengguna, kata_sandi):
        self.id = str(uuid.uuid4())  # Membuat UUID sebagai ID pengguna
        self.nama_pengguna = nama_pengguna
        self.__kata_sandi = kata_sandi  # Menggunakan __ untuk merahasiakan kata sandi
        self.pengeluaran = []

    def get_kata_sandi(self):
        return self.__kata_sandi

    def set_kata_sandi(self, kata_sandi_baru):
        self.__kata_sandi = kata_sandi_baru

    def daftar_pengguna(self):
        print(f"Pengguna '{self.nama_pengguna}' berhasil terdaftar.")

    def masuk(self, kata_sandi):
        if kata_sandi == self.__kata_sandi:
            print(f"Selamat datang, {self.nama_pengguna}!")
        else:
            print("Kata sandi salah. Silakan coba lagi.")

    def ubah_akun(self, nama_pengguna_lama, nama_pengguna_baru, kata_sandi_lama, kata_sandi_baru):
        if self.nama_pengguna == nama_pengguna_lama and self.__kata_sandi == kata_sandi_lama:
            self.nama_pengguna = nama_pengguna_baru
            self.__kata_sandi = kata_sandi_baru
            print("Akun berhasil diubah.")
        elif self.nama_pengguna != nama_pengguna_lama:
            print("Nama pengguna lama tidak sesuai.")
        elif self.__kata_sandi != kata_sandi_lama:
            print("Kata sandi lama tidak sesuai.")
        else:
            print("Perubahan akun tidak berhasil.")

class Pengeluaran:
    def __init__(self, deskripsi, jumlah):
        self.id = str(uuid.uuid4())  # Membuat UUID sebagai ID pengeluaran
        self.deskripsi = deskripsi
        self.jumlah = jumlah

class PencatatPengeluaran:
    def __init__(self):
        self.pengguna = []  # Menyimpan daftar pengguna
        self.pengguna_sekarang = None  # Menyimpan pengguna yang sedang aktif

    def daftar_pengguna(self, nama_pengguna, kata_sandi):
        for pengguna in self.pengguna:
            if pengguna.nama_pengguna == nama_pengguna:
                print("Nama pengguna sudah ada. Silakan pilih yang lain.")
                return

        pengguna_baru = Pengguna(nama_pengguna, kata_sandi)
        pengguna_baru.daftar_pengguna()
        self.pengguna.append(pengguna_baru)

    def masuk(self, nama_pengguna, kata_sandi):
        for pengguna in self.pengguna:
            if pengguna.nama_pengguna == nama_pengguna:
                pengguna.masuk(kata_sandi)
                if kata_sandi == pengguna.get_kata_sandi():
                    self.pengguna_sekarang = pengguna
                    return
                else:
                    return

        print("Nama pengguna tidak ditemukan atau kata sandi salah. Silakan coba lagi.")

    def kelola_pengeluaran(self, deskripsi, jumlah, ubah=False, id_pengeluaran=None):
        if not self.pengguna_sekarang:
            print("Silakan masuk terlebih dahulu.")
            return

        if ubah and id_pengeluaran:
            for pengeluaran in self.pengguna_sekarang.pengeluaran:
                if pengeluaran.id == id_pengeluaran:
                    pengeluaran.deskripsi, pengeluaran.jumlah = deskripsi, jumlah
                    print("Pengeluaran berhasil diubah.")
                    return

            print("Pengeluaran tidak ditemukan.")
        else:
            pengeluaran_baru = Pengeluaran(deskripsi, jumlah)
            self.pengguna_sekarang.pengeluaran.append(pengeluaran_baru)
            print("Pengeluaran berhasil ditambahkan.")

    def lihat_pengeluaran(self):
        if self.pengguna_sekarang and self.pengguna_sekarang.pengeluaran:
            print("Daftar Pengeluaran Anda:")
            for pengeluaran in self.pengguna_sekarang.pengeluaran:
                print("="*50)
                print(f"| => ID: {pengeluaran.id} \n| => Deskripsi: {pengeluaran.deskripsi} \n| => Jumlah: Rp. {pengeluaran.jumlah}")
                print("="*50)
        else:
            print("Tidak ada pengeluaran ditemukan.")

    def hapus_pengeluaran(self, id_pengeluaran):
        if self.pengguna_sekarang:
            for pengeluaran in self.pengguna_sekarang.pengeluaran:
                if pengeluaran.id == id_pengeluaran:
                    self.pengguna_sekarang.pengeluaran.remove(pengeluaran)
                    print("Pengeluaran berhasil dihapus.")
                    return

            print("Pengeluaran tidak ditemukan.")
        else:
            print("Silakan masuk terlebih dahulu.")

# Contoh penggunaan program
pencatat_pengeluaran = PencatatPengeluaran()

while True:
    if pencatat_pengeluaran.pengguna_sekarang is None:  # Jika belum ada pengguna yang masuk
        print("\n====== MENU ======")
        print("| 1. Daftar")
        print("| 2. Masuk")
        print("| 3. Keluar")
        print("==================")

        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == '1':
            nama_pengguna = input("Masukkan nama pengguna Anda: ")
            kata_sandi = getpass("Masukkan kata sandi Anda: ")
            pencatat_pengeluaran.daftar_pengguna(nama_pengguna, kata_sandi)

        elif pilihan == '2':
            nama_pengguna = input("Masukkan nama pengguna Anda: ")
            kata_sandi = getpass("Masukkan kata sandi Anda: ")
            pencatat_pengeluaran.masuk(nama_pengguna, kata_sandi)

        elif pilihan == '3':
            print("Keluar dari program. Sampai jumpa!")
            break

        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")

    else:  # Jika sudah ada pengguna yang masuk
        print("\n====== MENU ======")
        print("| 1. Tambah Pengeluaran")
        print("| 2. Lihat Pengeluaran")
        print("| 3. Ubah Pengeluaran")
        print("| 4. Hapus Pengeluaran")
        print("| 5. Ubah Akun")
        print("| 6. Keluar")
        print("==================")

        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == '1':
            deskripsi = input("Masukkan deskripsi pengeluaran: ")
            jumlah = float(input("Masukkan jumlah pengeluaran: "))
            pencatat_pengeluaran.kelola_pengeluaran(deskripsi, jumlah)

        elif pilihan == '2':
            pencatat_pengeluaran.lihat_pengeluaran()

        elif pilihan == '3':
            id_pengeluaran = input("Masukkan ID pengeluaran yang ingin diubah: ")
            deskripsi_baru = input("Masukkan deskripsi baru: ")
            jumlah_baru = float(input("Masukkan jumlah baru: "))
            pencatat_pengeluaran.kelola_pengeluaran(deskripsi_baru, jumlah_baru, ubah=True, id_pengeluaran=id_pengeluaran)

        elif pilihan == '4':
            id_pengeluaran = input("Masukkan ID pengeluaran yang ingin dihapus: ")
            pencatat_pengeluaran.hapus_pengeluaran(id_pengeluaran)

        elif pilihan == '5':
            nama_pengguna_lama = input("Masukkan nama pengguna lama: ")
            nama_pengguna_baru = input("Masukkan nama pengguna baru: ")
            kata_sandi_lama = getpass("Masukkan kata sandi lama Anda: ")
            kata_sandi_baru = getpass("Masukkan kata sandi baru Anda: ")
            pencatat_pengeluaran.pengguna_sekarang.ubah_akun(nama_pengguna_lama, nama_pengguna_baru, kata_sandi_lama, kata_sandi_baru)

        elif pilihan == '6':
            print("Keluar dari program. Sampai jumpa!")
            break

        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")