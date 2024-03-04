import os
os.system('cls')
import datetime
import pwinput
from prettytable import PrettyTable

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_after_node(self, prev_node_data, data):
        new_node = Node(data)
        current = self.head

        while current:
            if current.data["Nomor_SIM"] == prev_node_data:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

        print(f"Node dengan data {prev_node_data} tidak ditemukan.")

    def delete_at_beginning(self):
        if not self.head:
            print("List kosong. Tidak dapat menghapus.")
            return

        self.head = self.head.next

    def delete_at_end(self):
        if not self.head:
            print("List kosong. Tidak dapat menghapus.")
            return

        current = self.head
        prev = None

        while current.next:
            prev = current
            current = current.next

        if prev:
            prev.next = None
        else:
            self.head = None

    def delete_after_node(self, prev_node_data):
        current = self.head

        while current:
            if current.data["Nomor_SIM"] == prev_node_data and current.next:
                current.next = current.next.next
                return
            current = current.next

        print(f"Node dengan data {prev_node_data} tidak ditemukan atau tidak memiliki node setelahnya.")

    def display(self):
        table = PrettyTable()
        table.field_names = ["Nomor_SIM", "Nama", "Tempat/Tanggal Lahir", "Jenis_Kelamin","Golongan Darah", "Alamat","Provinsi","Jenis_SIM", "Tanggal Terbit", "Tanggal Expired"]

        current = self.head
        while current:
            data = current.data
            table.add_row([
                data["Nomor_SIM"],
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
            current = current.next

        print(table)

class Data_SIM:
    def __init__(self, Nama, Tempat_lahir, Tanggal_lahir, Jenis_Kelamin, Golongan_darah, Provinsi,Alamat,Jenis_SIM):
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
        nomor_urut = 1100
        return f"S{str(tahun_lahir)[-2:]}{self.Tanggal_lahir[3:5]}{self.Tanggal_lahir[:2]}{nomor_urut:03d}"

    def buat_sim(self):
        if self.nomor_SIM is None:
            self.nomor_SIM = self.generate_nomor_SIM()
            self.Tanggal_terbit = datetime.date.today()
            self.Tanggal_expired = self.Tanggal_terbit + datetime.timedelta(days=1825)

# Penggunaan
linked_list_SIM = LinkedList()

while True:
    print("==============================+ SISTEM PEMBUATAN SIM +===============================")
    print("|     Silahkan login terlebih dahulu admin:) jika ingin masuk dalam sistem Pulici   |")
    print("|      DILARANG KERAS UNTUK MENYEBARKAN DATA PRIBADI DALAM SISTEM KEPOLIISIAN!      |")
    print("|                          Sebar data = masuk lapas ehe                             |")
    print("==============================+ SISTEM PENDATAAN SIM +===============================")

    username = input("Masuk dulu bos :")
    password = pwinput.pwinput("Jangan sampai lupa password sendiri y :")

    if username == "Pulici" and password == "090913":
        print(f"Selamat datang di Sistem Khusus SIM, {username}")
        break
    else:
        print("MYDAY MYDAY KAMY SIAPA? KAMU BUKAN PULICIIII PASSWORD KAMU SALAH ULANG YOK!")

while True:
    print("\n==========+++ HOLA INI PEMBUATAN SIM ADMIN +++=============")
    print("|               1. Tambah data SIM baru                   |")
    print("|               2. Tampilkan Data SIM Kepolisian          |")
    print("|               3. Update Data SIM Kepolisian             |")
    print("|               4. Hapus Data SIM                         |")
    print("|               5. Keluar                                 |")
    print("===========+++ HOLA INI PENDATAAN SIM ADMIN +++============")

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

        # Create a new instance of Data_SIM
        SIM_baru = Data_SIM(Nama, Tempat_lahir, Tanggal_lahir, Jenis_Kelamin, Golongan_darah, Alamat, Provinsi, Jenis_SIM)
        SIM_baru.buat_sim()

        # Add data to the linked list based on user choice
        insert_option = input("Pilih opsi penambahan data (1. Di awal, 2. Di akhir, 3. Setelah Nomor SIM tertentu):")

        if insert_option == "1":
            linked_list_SIM.insert_at_beginning({
                "Nomor_SIM": SIM_baru.nomor_SIM,
                "Nama": SIM_baru.Nama,
                "Tempat_lahir": SIM_baru.Tempat_lahir,
                "Tanggal_lahir": SIM_baru.Tanggal_lahir,
                "Jenis_Kelamin": SIM_baru.Jenis_Kelamin,
                "Golongan_darah": SIM_baru.Golongan_darah,
                "Provinsi": SIM_baru.Provinsi,
                "Alamat": SIM_baru.Alamat,
                "Jenis_SIM": SIM_baru.Jenis_SIM,
                "Tanggal_terbit": str(SIM_baru.Tanggal_terbit),
                "Tanggal_expired": str(SIM_baru.Tanggal_expired)
            })
            print(f"{SIM_baru.Nama} berhasil ditambahkan di awal dalam data Kepolisian")

        elif insert_option == "2":
            linked_list_SIM.insert_at_end({
                "Nomor_SIM": SIM_baru.nomor_SIM,
                "Nama": SIM_baru.Nama,
                "Tempat_lahir": SIM_baru.Tempat_lahir,
                "Tanggal_lahir": SIM_baru.Tanggal_lahir,
                "Jenis_Kelamin": SIM_baru.Jenis_Kelamin,
                "Golongan_darah": SIM_baru.Golongan_darah,
                "Provinsi": SIM_baru.Provinsi,
                "Alamat": SIM_baru.Alamat,
                "Jenis_SIM": SIM_baru.Jenis_SIM,
                "Tanggal_terbit": str(SIM_baru.Tanggal_terbit),
                "Tanggal_expired": str(SIM_baru.Tanggal_expired)
            })
            print(f"{SIM_baru.Nama} berhasil ditambahkan di akhir dalam data Kepolisian")

        elif insert_option == "3":
            nomor_SIM_tentu = input("Masukkan Nomor SIM setelahnya: ")
            linked_list_SIM.insert_after_node(nomor_SIM_tentu, {
                "Nomor_SIM": SIM_baru.nomor_SIM,
                "Nama": SIM_baru.Nama,
                "Tempat_lahir": SIM_baru.Tempat_lahir,
                "Tanggal_lahir": SIM_baru.Tanggal_lahir,
                "Jenis_Kelamin": SIM_baru.Jenis_Kelamin,
                "Golongan_darah": SIM_baru.Golongan_darah,
                "Provinsi": SIM_baru.Provinsi,
                "Alamat": SIM_baru.Alamat,
                "Jenis_SIM": SIM_baru.Jenis_SIM,
                "Tanggal_terbit": str(SIM_baru.Tanggal_terbit),
                "Tanggal_expired": str(SIM_baru.Tanggal_expired)
            })
            print(f"{SIM_baru.Nama} berhasil ditambahkan setelah Nomor SIM {nomor_SIM_tentu} dalam data Kepolisian")

    elif Option == "2":
        linked_list_SIM.display()

    elif Option == "3":
        nomor_SIM = input("Masukkan Nomor SIM yang datanya akan di update: ")
        field = input("Masukkan data yang mau diperbarui: ")
        nilai_baru = input(f"Masukkan data baru untuk {field}:")
        linked_list_SIM.update_node(nomor_SIM, field, nilai_baru)

    elif Option == "4":
        delete_option = input("Pilih opsi penghapusan (1. Di awal, 2. Di akhir, 3. Setelah Nomor SIM tertentu): ")
        
        if delete_option == "1":
            linked_list_SIM.delete_at_beginning()
        elif delete_option == "2":
            linked_list_SIM.delete_at_end()
        elif delete_option == "3":
            nomor_SIM = input("Masukkan Nomor SIM setelahnya yang akan dihapus: ")
            linked_list_SIM.delete_after_node(nomor_SIM)
        else:
            print("Opsi penghapusan tidak valid.")

    elif Option == "5":
        print("\n========================================================")
        print(" |                                                       |")
        print(f"|                TERIMA KACIW {username}                |")
        print(" |           Selamat menjalani hari yang indah!          |")
        print(" |         semoga pengujian akhir dimudahkan eheq        |")
        print(" |                                                       |")
        print("==========================================================")
        break

    else:
        print("Pilihan tidak valid, pilih sekali lagi")
