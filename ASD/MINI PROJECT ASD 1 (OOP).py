import os
os.system('cls')
import datetime
import pwinput
import json
from prettytable import PrettyTable

class Data_SIM:
    def __init__(self, Nama, Tempat_lahir, Tanggal_lahir, Jenis_Kelamin,Golongan_darah, Provinsi,Alamat,Jenis_SIM):
        self.Nama = Nama
        self.Tempat_lahir = Tempat_lahir
        self.Tanggal_lahir = Tanggal_lahir
        self.Jenis_Kelamin = Jenis_Kelamin
        self.Golongan_darah = Golongan_darah
        self.Provinsi = Provinsi
        self.Alamat = Alamat
        self.Jenis_SIM = Jenis_SIM
        self.Tanggal_terbit = None
        self.Tanggal_expired = None
        self.nomor_SIM = None

    def generate_nomor_SIM(self):
        tahun_lahir = datetime.datetime.strptime(self.Tanggal_lahir, "%d-%m-%Y").year
        nomor_urut = 1011  # Nomor urut sebagai pembeda sim satu dengan yang lainnya semacam NIK, bisa diubah oleh Admin
        return f"S{str(tahun_lahir)[-2:]}{self.Tanggal_lahir[3:5]}{self.Tanggal_lahir[:2]}{nomor_urut:03d}" #Sebagai format nomor SIM
        #Format nomor SIM dengan dua angka belakang tahun lahir, bulan, dan tanggal lahir. Dengan nomor urut yang bisa diubah
        #Jika lahir di tgl/tahun 07-12-1989 maka format nomor SIM akan menjadi S89012071011 
        #Dimana huruf S dalam nomor SIM digunakan untuk melambangkan bahwa nomor tersebut adalah nomor identitas SIM 9Surat Izin Mengemudi)

    def buat_sim(self):
        if self.nomor_SIM is None:
            self.nomor_SIM = self.generate_nomor_SIM()
            self.Tanggal_terbit = datetime.date.today()
            self.Tanggal_expired = self.Tanggal_terbit + datetime.timedelta(days=1825)  # SIM berlaku selama 5 tahun

class Systeminfo_SIM:
    def __init__(self):
        self.Pendataan_SIM = {}
        self.admin_SIM = {"Pulici": "090913"}  # Buat Login sebagai Admin CRUD Pulici

        try:
            with open("Pendataan_SIM.json", "r") as file:
                self.Pendataan_SIM = json.load(file)
        except FileNotFoundError:
            pass

    def login(self, username, password):
        if username in self.admin_SIM and self.admin_SIM[username] == password:
            print(f"Selamat datang di pendataan SIM {username}")
            return True
        else:
            print("MYDAY MYDAY KAMU SIAPA?!KAMU BUKAN PULICIIII PASSWORD KAMU SALAH ULANGI LAGI!")
            return False

    def tambah_pengendara_SIM(self, Data_SIM):
        if Data_SIM.nomor_SIM not in self.Pendataan_SIM:
            self.Pendataan_SIM[Data_SIM.nomor_SIM] = {
                "Nama": Data_SIM.Nama,
                "Tempat_lahir": Data_SIM.Tempat_lahir,
                "Tanggal_lahir": Data_SIM.Tanggal_lahir,
                "Jenis_Kelamin" : Data_SIM.Jenis_Kelamin,
                "Golongan_darah": Data_SIM.Golongan_darah,
                "Provinsi" : Data_SIM.Provinsi,
                "Alamat": Data_SIM.Alamat,
                "Jenis_SIM" : Data_SIM.Jenis_SIM,
                "Tanggal_terbit": str(Data_SIM.Tanggal_terbit),
                "Tanggal_expired": str(Data_SIM.Tanggal_expired)
            }
            print(f"{Data_SIM.Nama} berhasil ditambahkan dalam data Kepolisian")
        else:
            print("Nomor SIM dan Data pengendara sudah ada dalam data")

    def tampilkan_Data_SIM(self):
        table = PrettyTable()
        table.field_names = ["Nomor SIM", "Nama", "Tempat/Tanggal Lahir", "Jenis_Kelamin","Golongan Darah", "Alamat","Provinsi","Jenis_SIM", "Tanggal Terbit", "Tanggal Expired"]

        for nomor_SIM, data in self.Pendataan_SIM.items():
            table.add_row([
                nomor_SIM,
                data["Nama"],
                f"{data['Tempat_lahir']}, {data['Tanggal_lahir']}",
                data["Jenis_Kelamin"],
                data["Golongan_darah"],
                data["Alamat"],
                data["Provinsi"],
                data["Jenis_SIM"],
                data["Tanggal_terbit"],
                data["Tanggal_expired"]
            ])

        print(table)

    def update_Data_SIM(self, nomor_SIM, field, nilai_baru):
        if nomor_SIM in self.Pendataan_SIM:
            if field in self.Pendataan_SIM[nomor_SIM]:
                self.Pendataan_SIM[nomor_SIM][field] = nilai_baru
                print(f"Data SIM dengan Nomor SIM {nomor_SIM} berhasil diperbarui")
            else:
                print(f"field {field} tidak valid")
        else:
            print(f"Data SIM dengan Nomor SIM {nomor_SIM} error not found")

    def delete_Data_SIM(self, nomor_SIM):
        if nomor_SIM in self.Pendataan_SIM:
            del self.Pendataan_SIM[nomor_SIM]
            print(f"Data SIM dengan nomor SIM {nomor_SIM} telah dihapus eksistensinya")
        else:
            print(f"Data SIM dengan Nomor SIM {nomor_SIM} error not found")

    def simpan_Data_SIM(self):
        with open("Pendataan_SIM.json", "w") as file:
            json.dump(self.Pendataan_SIM, file, indent=4)

# Penggunaan
sistem_SIM = Systeminfo_SIM()

while True:
    print("==============================+ SISTEM PEMBUATAN SIM +===============================")
    print("|     Silahkan login terlebih dahulu admin:) jika ingin masuk dalam sistem Pulici   |")
    print("|      DILARANG KERAS UNTUK MENYEBARKAN DATA PRIBADI DALAM SISTEM KEPOLIISIAN!      |")
    print("|                          Sebar data = masuk lapas ehe                             |")
    print("==============================+ SISTEM PENDATAAN SIM +===============================")

    username = input("Masuk dulu bos :")
    password = pwinput.pwinput("Jangan sampai lupa password sendiri y :")

    if sistem_SIM.login(username, password):
        break

while True:
    print("\n========+++ HOLA INI PEMBUATAN SIM ADMIN +++===========")
    print("|               1. Tambah data SIM baru                 |")
    print("|               2. Tampilkan Data SIM Kepolisian        |")
    print("|               3. Update Data SIM Kepolisian           |")
    print("|               4. Hapus Data SIM                       |")
    print("|               5. Keluar                               |")
    print("\n=======+++ HOLA INI PENDATAAN SIM ADMIN +++============")

    Option = input("Pilih menu (1/2/3/4/5):")

    if Option == "1":
        Nama = input("Nama: ")
        Tempat_lahir = input("Tempat lahir:")
        Tanggal_lahir = input("Tanggal lahir:")
        Jenis_Kelamin = input("Jenis_Kelamin:")
        Golongan_darah = input("Golongan darah:")
        Alamat = input("Alamat:")
        Provinsi = input("Provinsi:")
        Jenis_SIM = input("Jenis_SIM:")

        SIM_baru = Data_SIM(Nama, Tempat_lahir, Tanggal_lahir, Jenis_Kelamin,Golongan_darah, Alamat,Provinsi,Jenis_SIM)
        SIM_baru.buat_sim()  #Untuk menghasilkan nomor SIM, tanggal terbit, dan tanggal expired
        sistem_SIM.tambah_pengendara_SIM(SIM_baru)

    elif Option == "2":
        sistem_SIM.tampilkan_Data_SIM()

    elif Option == "3":
        nomor_SIM = input("Masukkan Nomor SIM yang datanya akan di update: ")
        field = input("Masukkan data yang mau diperbarui: ")
        nilai_baru = input(f"Masukkan data baru untuk {field}:")
        sistem_SIM.update_Data_SIM(nomor_SIM, field, nilai_baru)

    elif Option == "4":
        nomor_SIM = input("Masukkan nomor SIM yang akan dihapus:")
        sistem_SIM.delete_Data_SIM(nomor_SIM)

    elif Option == "5":
        print("Program selesai")
        sistem_SIM.simpan_Data_SIM()
        break
        exit()

    else:
        print("Pilihan tidak valid, pilih sekali lagi")
