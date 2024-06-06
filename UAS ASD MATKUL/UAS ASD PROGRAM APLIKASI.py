import os
os.system('cls')
from prettytable import PrettyTable
import datetime
import pwinput
import time


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def tambah_barang(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def cek_duplikasi_id(self, ID):
        current = self.head
        while current:
            if current.data["ID"] == ID:
                return True
            current = current.next
        return False

    def cek_duplikasi_nama(self, nama):
        current = self.head
        while current:
            if current.data["Nama APPS"] == nama:
                return True
            current = current.next
        return False

    def tambah_akun(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def hapus_barang(self, ID):
        if not self.head:
            print("List kosong. Tidak dapat menghapus.")
            return
        if self.head.data["ID"] == ID:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data["ID"] == ID:
                current.next = current.next.next
                return
            current = current.next
        print("Barang tidak ditemukan.")

    def _convert_to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
    
    def update_barang(self, ID, new_name=None, new_quantity=None, new_price=None, new_waktu_awal=None, new_waktu_akhir=None):
        current = self.head
        while current:
            if current.data["ID"] == ID:
                if new_name:
                    current.data["Nama APPS"] = new_name
                if new_price:
                    current.data["Harga"] = new_price
                if new_quantity:
                    current.data["Stok"] = new_quantity
                if new_waktu_awal:
                    current.data["Waktu_awal_premium"] = new_waktu_awal
                if new_waktu_akhir:
                    current.data["Waktu_akhir_premium"] = new_waktu_akhir
                print("Barang berhasil diupdate.")
                return
            current = current.next
        print("Barang tidak ditemukan.")

    def check_saldo(self):
        current = self.head
        if not current:
            print("Tidak ada customer yang terdaftar.")
            return

        while current:
            akun_pengguna = current.data
            username = akun_pengguna["Username"]
            saldo = akun_pengguna["Saldo"]
            print(f"Nama Pengguna: {username}")
            print(f"Saldo: Rp{saldo}")
            print("------------------")
            current = current.next

    def quick_sort(self, reverse=False):
        if self.head is None or self.head.next is None:
            return
        sorted_list = None
        current = self.head
        while current:
            next_node = current.next
            if sorted_list is None or (not reverse and current.data["Harga"] < sorted_list.data["Harga"]) or (reverse and current.data["Harga"] > sorted_list.data["Harga"]):
                current.next = sorted_list
                sorted_list = current
            else:
                temp = sorted_list
                while temp.next and ((not reverse and temp.next.data["Harga"] < current.data["Harga"]) or (reverse and temp.next.data["Harga"] > current.data["Harga"])):
                    temp = temp.next
                current.next = temp.next
                temp.next = current
            current = next_node
        self.head = sorted_list

    def jump_search(self, key, value):
        data_found = []
        current = self.head
        while current:
            if current.data.get(key) == value:
                data_found.append(current.data)
                break  # Langsung keluar dari loop setelah kunci ditemukan
            current = current.next
        if not data_found:
            print(f"{key} with value {value} not found.")
        else:
            # Tentukan nama-nama kolom berdasarkan kunci di dalam data
            column_names = list(data_found[0].keys())
            
            # Buat objek PrettyTable dan tentukan nama-nama kolom
            table = PrettyTable()
            table.field_names = column_names
            
            # Tambahkan baris ke dalam tabel
            for data in data_found:
                table.add_row([data[col] for col in column_names])
            
            print("Result:")
            print(table)
        return data_found

        
    def display(self):
        if not self.head:
            print("Tidak ada data, data kosong")
            return
        table = PrettyTable()
        table.field_names = ["ID", "Nama APPS", "Harga", "Stok","Waktu awal premium", "Waktu akhir premium"]

        current = self.head
        while current:
            data = current.data
            table.add_row([
                data["ID"],
                data["Nama APPS"],
                data["Harga"],
                data["Stok"],
                data["Waktu_awal_premium"],
                data["Waktu_akhir_premium"]
            ])
            current = current.next
        print(table)

class CHIPIStore:
    def __init__(self):
        #AKUN PERMANEN ADMIN
        self.admin_username = "Kiruki"
        self.admin_password = "Alohomora"

        #DATA PERMANEN AKUN CUSTOMER
        self.customers = LinkedList()
        self.customers.tambah_akun({"Username": "Niere", "Password": "090913", "Saldo": 200000, "Gender": "Perempuan","Usia": 20})
        self.customers.tambah_akun({"Username": "Mahameru", "Password": "koffe", "Saldo": 350000, "Gender": "Pria","Usia": 28})

        #DATA PERMANEN BARANG APPS PREMIUM
        self.barang = LinkedList()
        self.barang.tambah_barang({"ID": 1001, "Nama APPS": "Canva", "Harga": 15000, "Stok": 5,"Waktu_awal_premium": datetime.datetime.now().strftime('%Y-%m-%d'), "Waktu_akhir_premium": (datetime.datetime.now() + datetime.timedelta(days=90)).strftime('%Y-%m-%d')})
        self.barang.tambah_barang({"ID": 1002, "Nama APPS": "Netflix", "Harga": 38000, "Stok": 7,"Waktu_awal_premium": datetime.datetime.now().strftime('%Y-%m-%d'), "Waktu_akhir_premium": (datetime.datetime.now() + datetime.timedelta(days=60)).strftime('%Y-%m-%d')})
        self.barang.tambah_barang({"ID": 1003, "Nama APPS": "Disney", "Harga": 45000, "Stok": 4,"Waktu_awal_premium": datetime.datetime.now().strftime('%Y-%m-%d'), "Waktu_akhir_premium": (datetime.datetime.now() + datetime.timedelta(days=30)).strftime('%Y-%m-%d')})
        self.barang.tambah_barang({"ID": 1004, "Nama APPS": "ChatGPT", "Harga": 35000, "Stok": 6,"Waktu_awal_premium": datetime.datetime.now().strftime('%Y-%m-%d'), "Waktu_akhir_premium": (datetime.datetime.now() + datetime.timedelta(days=90)).strftime('%Y-%m-%d')})
        self.barang.tambah_barang({"ID": 1005, "Nama APPS": "Spotify", "Harga": 23000, "Stok": 8,"Waktu_awal_premium": datetime.datetime.now().strftime('%Y-%m-%d'), "Waktu_akhir_premium": (datetime.datetime.now() + datetime.timedelta(days=30)).strftime('%Y-%m-%d')})
        self.barang.tambah_barang({"ID": 1006, "Nama APPS": "VIDIO.COM", "Harga": 35000, "Stok": 6,"Waktu_awal_premium": datetime.datetime.now().strftime('%Y-%m-%d'), "Waktu_akhir_premium": (datetime.datetime.now() + datetime.timedelta(days=30)).strftime('%Y-%m-%d')})
        self.barang.tambah_barang({"ID": 1007, "Nama APPS": "LOK LOK", "Harga": 15000, "Stok": 3,"Waktu_awal_premium": datetime.datetime.now().strftime('%Y-%m-%d'), "Waktu_akhir_premium": (datetime.datetime.now() + datetime.timedelta(days=30)).strftime('%Y-%m-%d')})
        self.barang.tambah_barang({"ID": 1008, "Nama APPS": "BS STATION", "Harga": 43000, "Stok": 4,"Waktu_awal_premium": datetime.datetime.now().strftime('%Y-%m-%d'), "Waktu_akhir_premium": (datetime.datetime.now() + datetime.timedelta(days=30)).strftime('%Y-%m-%d')})
        self.barang.tambah_barang({"ID": 1009, "Nama APPS": "YOUTUBE", "Harga": 18000, "Stok": 2,"Waktu_awal_premium": datetime.datetime.now().strftime('%Y-%m-%d'), "Waktu_akhir_premium": (datetime.datetime.now() + datetime.timedelta(days=30)).strftime('%Y-%m-%d')})
        self.barang.tambah_barang({"ID": 10010, "Nama APPS": "VIU", "Harga": 16000, "Stok": 4,"Waktu_awal_premium": datetime.datetime.now().strftime('%Y-%m-%d'), "Waktu_akhir_premium": (datetime.datetime.now() + datetime.timedelta(days=30)).strftime('%Y-%m-%d')})
        self.barang.tambah_barang({"ID": 10011, "Nama APPS": "IQIYI", "Harga": 36000, "Stok": 2,"Waktu_awal_premium": datetime.datetime.now().strftime('%Y-%m-%d'), "Waktu_akhir_premium": (datetime.datetime.now() + datetime.timedelta(days=30)).strftime('%Y-%m-%d')})


        self.min_diskon = {100000:0.1, 250000:0.15, 350000:0.25}
        self.working_hours = (8, 16)

    def tambah_customer(self, username, password, saldo, gender, usia):
        self.customers.tambah_akun({"Username": username, "Password": password, "Saldo": saldo, "Gender": gender, "Usia": usia})
    
    def add_barang(self, ID, name, price, stok):
        self.barang.tambah_barang({"ID": ID, "Nama APPS": name, "Harga": price, "Stok" : stok,"Waktu_awal_premium": datetime.date.today().strftime('%Y-%m-%d'), "Waktu_akhir_premium": (datetime.datetime.now() + datetime.timedelta(days=30)).strftime('%Y-%m-%d')})

    def is_working_hours(self):
        now = datetime.datetime.now()
        return self.working_hours[0] <= now.hour < self.working_hours[1]

    def authenticate_customer(self):
        username = input("Username: ")
        password = input("Password: ")
        current = self.customers.head
        while current:
            if current.data["Username"] == username and current.data["Password"] == password:
                return username
            current = current.next
        return None

    def login_admin(self):
        kesempatan = 0
        max_kesempatan = 3

        while kesempatan < max_kesempatan:
                print('''\n
                        ================================================
                        ||          HELLO OUR DEAR ADMIN STORE^^      ||
                        ||>>>>>>>>>>>>  CHIPI CHAPA STORE  <<<<<<<<<<<||
                        ||                                            ||
                        ||                                            ||
                        ||-----------------LOGIN ADMIN----------------||
                        ||                                            ||
                        ||                                            ||
                        ================================================\n''')
                
                username = input("Masukkan akun anda Admin:")
                password = pwinput.pwinput("Masukkan password anda:")

                if username == "Kiruki" and password == "Alohomora":
                    print(f"Selamat datang ADMIN CHIPI CHAPA STORE, {username}")
                    return username
                else:
                    kesempatan += 1
                    print("MYDAY MYDAY WHO THE HELL ARE YOUUUU?????? YOU'RE NOT ADMIN")

                    if kesempatan == max_kesempatan:
                        print("\nAnda selalu keliru nih curiga hacker ketunda ya bro")
                        for i in range(10, 0, -1):
                            print(f"\nTunggu pemeriksaan sebentar ya untuk login, tunggu {i} detik", end="\r")
                            time.sleep(1)

                        print("Jeda waktu pemeriksaan selesai! Silahkan login kembali")
                        kesempatan = 0
                        continue
            


    def login_customer(self):
        kesempatan = 0
        max_kesempatan = 3

        while kesempatan < max_kesempatan:
                print('''\n
                        ================================================
                        ||          HELLO OUR DEAR CUSTOMER^^         ||
                        ||>>>>>>>>>>>>  CHIPI CHAPA STORE  <<<<<<<<<<<||
                        ||                                            ||
                        ||                                            ||
                        ||---------------LOGIN CUSTOMER---------------||
                        ||                                            ||
                        ||                                            ||
                        ================================================\n''')
                
                
                username = input('Masukkan akun pengguna anda: ')
                password = pwinput.pwinput('Masukkan Password akun anda: ')

                user_account = self.customers.jump_search("Username", username)
                if user_account and user_account[0]["Password"] == password:
                    if user_account and user_account[0]["Password"] == password:
                        gender = user_account[0].get("Gender","unknown")
                        usia = user_account[0].get("Usia", 0)
                        if gender == "Pria":
                            if 17 <= usia <= 20:
                                panggilan = "Kak"
                            elif 20 <= usia <= 28:
                                panggilan = "Mas"
                            elif 28 <= usia <= 65:
                                panggilan = "Pak"
                        elif gender == "Perempuan":
                            if 17 <= usia <= 20:
                                panggilan = "Kak"
                            elif 20 <= usia <= 28:
                                panggilan = "Mbak"
                            elif 28 <= usia <= 65:
                                panggilan = "Ibu"
                            else:
                                panggilan = "Nyonya"
                        else:
                            panggilan = "Tuan"
                    
                    print(f'''\n
                        ======================================================
                        ||                                                  ||
                        ||>>>>>>>>>>>>>>    HELLO! SWEETIE     <<<<<<<<<<<<<||
                                        Selamat datang {panggilan} {username}!      
                        ||                                                  ||
                        ||                                                  ||    
                        ======================================================\n''')
                    return username
                else:
                    kesempatan += 1
                    print('\nAnda selalu keliru, maaf tapi proses login anda tertunda')

                    if kesempatan == max_kesempatan:
                        print("\nAnda selalu keliru nih curiga hacker ketunda ya bro")
                        for i in range(10, 0, -1):
                            print(f"\nTunggu pemeriksaan sebentar ya untuk login, tunggu {i} detik", end="\r")
                            time.sleep(1)

                        print("Jeda waktu pemeriksaan selesai! Silahkan login kembali")
                        kesempatan = 0
                        continue


    def top_up_saldo(self, username):
        while True:
            print('''\n
                    ==============================================
                    ‖     HELLO DEAR OUR CUSTOMER! WELCOME!      ‖
                    ‖>>>>>>>>>>>   CHIPI CHAPA store! <<<<<<<<<<<‖
                    ‖                                            ‖
                    ‖----------------TOP-UP SALDO----------------‖
                    ‖                                            ‖
                    ==============================================\n''')
            jumlah_topup = int(input('Masukkan jumlah saldo untuk di top-up:'))
            if jumlah_topup > 0: 
                user_account = self.customers.jump_search("Username", username)
                if user_account:  
                    user_account[0]["Saldo"] += jumlah_topup
                    print(f"Top-up saldo berhasil. Saldo sekarang: {user_account[0]['Saldo']}")
                    break
                else:
                    print("Username tidak ditemukan.")
            else:
                print("Jumlah top-up harus lebih dari 0.")

    def pembelian_customer(self, username):
        if not self.is_working_hours():
            print("Pembelian hanya bisa dilakukan pada jam kerja (08.00 - 16.00).")
            return
        self.barang.display()
        cart = {}
        while True:
            print('''\n
                    ==============================================
                    ‖       HELLO DEAR OUR CUSTOMER WELCOME      ‖
                    ‖>>>>>>>>>>>   CHIPI CHAPA store  <<<<<<<<<<<‖
                    ‖                                            ‖
                    ‖------------------TRANSAKSI-----------------‖
                    ‖                                            ‖
                    ==============================================\n''')

            
            pilih_ID = int(input("Masukkan ID APPS yang mau dibeli:"))

            APPS_pilih = self.barang.jump_search("ID", pilih_ID)
            if not APPS_pilih:
                print("APK tidak ditemukan, harap masukkan ID yang benar")
                continue

            try:
                quantity = int(input("Masukkan jumlah: "))
                if quantity <= 0:
                    print("Jumlah harus lebih dari 0.")
                    continue
            except ValueError:
                print("Jumlah harus berupa angka.")
                continue

            # Periksa apakah stok tersedia
            for APPS in APPS_pilih:
                if APPS["Stok"] < quantity:
                    print("Jumlah barang tidak mencukupi.")
                    break
            else:
                # Gunakan ID produk bersama dengan jumlah sebagai kunci
                cart[pilih_ID] = cart.get(pilih_ID, 0) + quantity

            total_price = sum(self.barang.jump_search("ID", ID)[0]["Harga"] * qty for ID, qty in cart.items())
            
            applicable_discount = 0
            for threshold, discount in self.min_diskon.items():
                if total_price >= threshold:
                    applicable_discount = discount

            total_price_after_discount = total_price * (1 - applicable_discount)

            current_customer = self.customers.jump_search("Username", username)[0]
            if current_customer["Saldo"] < total_price_after_discount:
                print("Saldo e-money tidak mencukupi.")
                break

            tambah_barang = input("Apakah Anda ingin menambah barang lain? (y/n): ")
            if tambah_barang.lower() == 'n':
                current_customer["Saldo"] -= total_price_after_discount
                for ID, qty in cart.items():
                    APPS = self.barang.jump_search("ID", ID)
                    if APPS:
                        APPS[0]["Stok"] -= qty

                print(f"Pembelian berhasil. Total harga setelah diskon: Rp {total_price_after_discount:.2f}")
                
                # Cetak invoice
                self.cetak_invoice(username, cart, total_price, total_price_after_discount)
                break

    def cetak_invoice(self, username, cart, total_price, total_price_after_discount):
        now = datetime.datetime.now()
        invoice_id = now.strftime('%Y%m%d%H%M%S')
        invoice_date = now.strftime('%Y-%m-%d %H:%M:%S')

        print(f'''\n
            ================================================================
            ||                                                            ||
            ||------------>    STRUK PEMBAYARAN PELANGGAN      <----------||
            ||                                                            ||
            ||                   ID Struk : {invoice_id}                  ||
            ||                  Nama pembeli : {username}                 ||
            ||               Waktu transaksi : {invoice_date}             ||
            ||                     Rincian Pembelian :                    ||
            ||              Normal Price : Rp {total_price:.2f}           ||
            ||      Discount Price : Rp {total_price_after_discount:.2f}  ||
            ================================================================\n''')
        
        table = PrettyTable()
        table.field_names = ["ID", "Nama APPS", "Harga", "Jumlah", "Subtotal"]
        
        for ID, qty in cart.items():
            APPS = self.barang.jump_search("ID", ID)[0]
            subtotal = APPS["Harga"] * qty
            table.add_row([ID, APPS["Nama APPS"], APPS["Harga"], qty, subtotal])

        print(table)


    def admin_menu(self):
        while True:
            os.system('cls')
            print('''
            ================================================
            ||               ADMIN MENU                   ||
            ================================================
            1. Tambah Barang
            2. Hapus Barang
            3. Update Barang
            4. Tampilkan Barang
            5. Urutkan Barang Berdasarkan Harga
            6. Cari barang
            7. Keluar
            ================================================
            ''')
            Pilihan = input("Pilih menu: ")
            if Pilihan == '1':
                try:
                    ID = int(input("Masukkan ID barang: "))
                    nama = input("Masukkan nama barang: ")

                    if self.barang.cek_duplikasi_id(ID):
                        print("ID barang sudah ada. Harap masukkan ID yang berbeda.")
                        break

                    if self.barang.cek_duplikasi_nama(nama):
                        print("Nama barang sudah ada. Harap masukkan nama yang berbeda.")
                        break

                    harga = int(input("Masukkan harga barang: "))
                    stok = int(input("Masukkan stok barang: "))
                    self.barang.tambah({"ID": ID, "Nama APPS": nama, "Harga": harga, "Stok": stok, "Waktu_awal_premium": datetime.datetime.now().strftime('%Y-%m-%d'), "Waktu_akhir_premium": (datetime.datetime.now() + datetime.timedelta(days=30)).strftime('%Y-%m-%d')})
                    print("Barang berhasil ditambahkan.")
                except ValueError:
                    print("Input tidak valid. Pastikan ID, harga, dan stok berupa angka.")
            elif Pilihan == '2':
                try:
                    ID = int(input("Masukkan ID barang yang ingin dihapus: "))
                    self.barang.hapus_barang(ID)
                except ValueError:
                    print("Input tidak valid. Harus berupa angka.")
            elif Pilihan == '3':
                try:
                    ID = int(input("Masukkan ID barang yang ingin diupdate: "))
                    nama = input("Masukkan nama baru (tekan enter untuk melewati): ")
                    harga = input("Masukkan harga baru (tekan enter untuk melewati): ")
                    stok = input("Masukkan stok baru (tekan enter untuk melewati): ")
                    waktu_awal = input("Masukkan waktu awal premium baru (tekan enter untuk melewati): ")
                    waktu_akhir = input("Masukkan waktu akhir premium baru (tekan enter untuk melewati): ")

                    harga = int(harga) if harga else None
                    stok = int(stok) if stok else None

                    self.barang.update_barang(ID, new_name=nama or None, new_price=harga, new_quantity=stok, new_waktu_awal=waktu_awal or None, new_waktu_akhir=waktu_akhir or None)
                except ValueError:
                    print("Input tidak valid. Pastikan ID, harga, dan stok berupa angka.")
            elif Pilihan == '4':
                self.barang.display()
            elif Pilihan == '5':
                reverse = input("Urutkan dari harga tertinggi? (y/n): ") == 'y'
                self.barang.quick_sort(reverse=reverse)
                print("Barang berhasil diurutkan.")
            elif Pilihan == '6':
                print("Pilih metode pencarian:")
                print("1. Cari berdasarkan ID")
                print("2. Cari berdasarkan Nama APPS")
                search_Pilihan = input("Pilih metode pencarian: ")
                if search_Pilihan == '1':
                    try:
                        nilai = int(input("Masukkan ID pencarian: "))
                        hasil_pencarian = self.barang.jump_search("ID", nilai)
                    except ValueError:
                        print("ID harus berupa angka.")
                        hasil_pencarian = None
                elif search_Pilihan == '2':
                    nilai = input("Masukkan Nama APPS pencarian: ")
                    hasil_pencarian = self.barang.jump_search("Nama APPS", nilai)
                else:
                    print("Metode pencarian tidak valid.")
                    hasil_pencarian = None
                
                if hasil_pencarian:
                    print("Barang ditemukan:")
                else:
                    print("Barang tidak ditemukan.")

            elif Pilihan == '7':
                break
            else:
                print("Pilihan tidak valid.")
            input("Tekan Enter untuk melanjutkan...")

    def customer_menu(self, username):
        while True:
            print('''
            ================================================
            ||              CUSTOMER MENU                 ||
            ================================================
            1. Lihat Barang
            2. Beli Barang
            3. Top-Up saldo
            4. Check Saldo
            5. Keluar
            ================================================
            ''')
            Pilihan = input("Pilih menu: ")
            if Pilihan == '1':
                self.barang.display()
            elif Pilihan == '2':
                self.pembelian_customer(username)
            elif Pilihan == '3':
                self.top_up_saldo(username)
            elif Pilihan == '4':
                self.customers.check_saldo()
            elif Pilihan == '5':
                break
            else:
                print("Pilihan tidak valid.")
            input("Tekan Enter untuk melanjutkan...")

    def main(self):
        while True:
            try:
                print('----------------------------------------')
                print('|    >>>>>>>>>Welcome bro!<<<<<<<<<    |')
                print('|--------------------------------------|')
                print('|            1. Login Admin            |')
                print('|            2. Login Customer         |')
                print('|            3. Regis Customer         |')
                print('|            4. Keluar                 |')
                print('|                                      |')
                print('----------------------------------------')

                Pilihan = input("Pilih menu: ")
                if Pilihan == '1':
                        admin = self.login_admin()
                        if admin:
                            self.admin_menu()
                        else:
                            print("Autentikasi gagal. Username atau password salah.")
                elif Pilihan == '2':
                        username = self.login_customer()
                        if username:
                            self.customer_menu(username)
                        else:
                            print("Autentikasi gagal. Username atau password salah.")
                elif Pilihan == '3':
                    username = input("Username: ")
                    password = input("Password: ")
                    saldo = int(input("Saldo e-money: "))
                    print("Pilih gender anda:")
                    print("1. Pria")
                    print("2. Perempuan")
                    gender_pilih = input("Masukkan Pilihan anda: ")
                    gender = "Pria" if gender_pilih == "1" else "Perempuan"
                    usia = int(input("Masukkan usia anda: "))
                    self.tambah_customer(username, password, saldo, gender, usia)  # Perubahan di sini
                    print("Customer berhasil didaftarkan.")
                elif Pilihan == '4':
                        print('''\n
                                =============================================================
                                ||>>>>  Terima kasih telah menggunakan aplikasi kami   <<<<||
                                =============================================================                                            
                                ||        ---> Silahkan Datang kembali!:))))))))<---       ||
                                =============================================================\n''')
                        break
                else:
                    print("Pilihan tidak valid.")
                    input("Tekan Enter untuk melanjutkan...")

            except ValueError as rawr:
                print("ERROR ON APLIKASI BRO", rawr)
        


app = CHIPIStore()
app.main()

