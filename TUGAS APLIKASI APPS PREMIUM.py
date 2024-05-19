import os
os.system('cls')
from prettytable import PrettyTable
import datetime
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
    
    def update_barang(self, ID, new_name=None, new_quantity=None, new_price=None, new_category=None):
        current = self.head
        while current:
            if current.data["ID"] == ID:
                if new_name:
                    current.data["Nama APPS"] = new_name
                if new_price:
                    current.data["Harga"] = new_price
                if new_quantity:
                    current.data["Stok"] = new_quantity
                if new_quantity:
                    current.data["Waktu_awal_premium"] = new_quantity
                if new_category:
                    current.data["Waktu_akhir_premium"] = new_category
                print("Barang berhasil diupdate.")
                return
            current = current.next
        print("Barang tidak ditemukan.")

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
        print(f"Searching for {key} with value {value}...")
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
            print(f"Result: {data_found}")
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
        self.customers.tambah_akun({"Username": "Niere", "Password": "090913", "Saldo": 200000})
        self.customers.tambah_akun({"Username": "Mahameru", "Password": "koffe", "Saldo": 350000})

        #DATA PERMANEN BARANG APPS PREMIUM
        self.barang = LinkedList()
        self.barang.tambah_barang({"ID": 1001, "Nama APPS": "Canva", "Harga": 15000, "Stok": 5,"Waktu_awal_premium": datetime.datetime.now().strftime('%Y-%m-%d'), "Waktu_akhir_premium": (datetime.datetime.now() + datetime.timedelta(days=30)).strftime('%Y-%m-%d')})
        self.barang.tambah_barang({"ID": 1002, "Nama APPS": "Netflix", "Harga": 38000, "Stok": 7,"Waktu_awal_premium": datetime.datetime.now().strftime('%Y-%m-%d'), "Waktu_akhir_premium": (datetime.datetime.now() + datetime.timedelta(days=30)).strftime('%Y-%m-%d')})
        self.barang.tambah_barang({"ID": 1003, "Nama APPS": "Disney", "Harga": 45000, "Stok": 4,"Waktu_awal_premium": datetime.datetime.now().strftime('%Y-%m-%d'), "Waktu_akhir_premium": (datetime.datetime.now() + datetime.timedelta(days=30)).strftime('%Y-%m-%d')})
        self.barang.tambah_barang({"ID": 1004, "Nama APPS": "ChatGPT", "Harga": 35000, "Stok": 6,"Waktu_awal_premium": datetime.datetime.now().strftime('%Y-%m-%d'), "Waktu_akhir_premium": (datetime.datetime.now() + datetime.timedelta(days=30)).strftime('%Y-%m-%d')})
        self.barang.tambah_barang({"ID": 1005, "Nama APPS": "Spotify", "Harga": 23000, "Stok": 8,"Waktu_awal_premium": datetime.datetime.now().strftime('%Y-%m-%d'), "Waktu_akhir_premium": (datetime.datetime.now() + datetime.timedelta(days=30)).strftime('%Y-%m-%d')})
        self.barang.tambah_barang({"ID": 1006, "Nama APPS": "VIDIO.COM", "Harga": 35000, "Stok": 6,"Waktu_awal_premium": datetime.datetime.now().strftime('%Y-%m-%d'), "Waktu_akhir_premium": (datetime.datetime.now() + datetime.timedelta(days=30)).strftime('%Y-%m-%d')})
        self.barang.tambah_barang({"ID": 1007, "Nama APPS": "LOK LOK", "Harga": 15000, "Stok": 3,"Waktu_awal_premium": datetime.datetime.now().strftime('%Y-%m-%d'), "Waktu_akhir_premium": (datetime.datetime.now() + datetime.timedelta(days=30)).strftime('%Y-%m-%d')})
        self.barang.tambah_barang({"ID": 1008, "Nama APPS": "BS STATION", "Harga": 43000, "Stok": 4,"Waktu_awal_premium": datetime.datetime.now().strftime('%Y-%m-%d'), "Waktu_akhir_premium": (datetime.datetime.now() + datetime.timedelta(days=30)).strftime('%Y-%m-%d')})
        self.barang.tambah_barang({"ID": 1009, "Nama APPS": "YOUTUBE", "Harga": 18000, "Stok": 2,"Waktu_awal_premium": datetime.datetime.now().strftime('%Y-%m-%d'), "Waktu_akhir_premium": (datetime.datetime.now() + datetime.timedelta(days=30)).strftime('%Y-%m-%d')})
        self.barang.tambah_barang({"ID": 10010, "Nama APPS": "VIU", "Harga": 16000, "Stok": 4,"Waktu_awal_premium": datetime.datetime.now().strftime('%Y-%m-%d'), "Waktu_akhir_premium": (datetime.datetime.now() + datetime.timedelta(days=30)).strftime('%Y-%m-%d')})
        self.barang.tambah_barang({"ID": 10011, "Nama APPS": "IQIYI", "Harga": 36000, "Stok": 2,"Waktu_awal_premium": datetime.datetime.now().strftime('%Y-%m-%d'), "Waktu_akhir_premium": (datetime.datetime.now() + datetime.timedelta(days=30)).strftime('%Y-%m-%d')})
        

        self.min_diskon = 100000
        self.rate_diskon = 0.1
        self.working_hours = (8, 16)

    def tambah_customer(self, Username, password, saldo):
        self.customers.tambah_akun({"Username": Username, "Password": password, "Saldo" : saldo})

    def add_barang(self, ID, name, price, stok):
        self.barang.tambah_barang({"ID": ID, "Nama APPS": name, "Harga": price, "Stok" : stok,"Waktu_awal_premium": datetime.date.today().strftime('%Y-%m-%d'), "Waktu_akhir_premium": datetime.date.today().strftime('%Y-%m-%d')})

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
            password = input("Masukkan password anda:")

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
            password = input('Masukkan Password akun anda: ')

            user_account = self.customers.jump_search("Username", username)

            if user_account and user_account[0]["Password"] == password:
                print(f'\nLogin berhasil! Selamat datang {username}')
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

            try:
                pilih_ID = input("Masukkan ID APPS yang mau dibeli:")
                if not pilih_ID.isnumeric():
                    print("ID harus berupa angka.")
                    continue
            except ValueError:
                print("ID harus berupa angka.")
                continue

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
                cart[(pilih_ID, quantity)] = APPS["Harga"] * quantity

            total_price = sum(price for price in cart.values())
            if total_price >= self.min_diskon:
                total_price *= (1 - self.rate_diskon)
            elif self.customers.jump_search("Username", username)[0]["Saldo"] < total_price:
                print("Saldo e-money tidak mencukupi.")
            else:
                self.customers.jump_search("Username", username)[0]["Saldo"] -= total_price
                for (APPS_ID, qty), price in cart.items():
                    APPS = self.barang.jump_search("ID", APPS_ID)
                    if APPS:
                        # Kurangi jumlah barang yang tersedia di dalam stok
                        APPS[0]["Stok"] -= qty
                print(f"Pembelian berhasil. Total harga: Rp {total_price:.2f}")
                break



            total_price = sum(APPS["Harga"] * qty for APPS_ID, qty in cart.items() for APPS in self.barang.jump_search("ID", APPS_ID))
            if total_price >= self.min_diskon:
                total_price *= (1 - self.rate_diskon)
            elif self.customers.jump_search("Username", username)[0]["Saldo"] < total_price:
                print("Saldo e-money tidak mencukupi.")
            else:
                self.customers.jump_search("Username", username)[0]["Saldo"] -= total_price
                for APPS_ID, qty in cart.items():
                    for APPS in self.barang.jump_search("ID", APPS_ID):
                        # Kurangi jumlah barang yang tersedia di dalam stok
                        APPS["Stok"] -= qty
                print(f"Pembelian berhasil. Total harga: Rp {total_price:.2f}")
                break


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
            6. Keluar
            ================================================
            ''')
            choice = input("Pilih menu: ")
            if choice == '1':
                ID = input("ID:")
                name = input("Nama Barang: ")
                price = int(input("Harga: "))
                stok = int(input("Stok:"))
                self.add_barang(ID, name, price, stok)
                print("Barang berhasil ditambahkan.")
            elif choice == '2':
                name = input("Nama Barang yang ingin dihapus: ")
                self.barang.hapus_barang(name)
                print("Barang berhasil dihapus.")
            elif choice == '3':
                ID = input("Nama Barang yang ingin diupdate: ")
                new_name = input("Nama Baru (kosongkan jika tidak diubah): ")
                new_quantity = input("Jumlah Baru (kosongkan jika tidak diubah): ")
                new_price = input("Harga Baru (kosongkan jika tidak diubah): ")
                new_category = input("Kategori Baru (kosongkan jika tidak diubah): ")
                self.barang.update_barang(ID, new_name or None, int(new_quantity) if new_quantity else None, int(new_price) if new_price else None, new_category or None)
            elif choice == '4':
                self.barang.display()
            elif choice == '5':
                reverse = input("Urutkan dari harga tertinggi? (y/n): ") == 'y'
                self.barang.quick_sort(reverse=reverse)
                print("Barang berhasil diurutkan.")
            elif choice == '6':
                break
            else:
                print("Pilihan tidak valid.")
            input("Tekan Enter untuk melanjutkan...")

    def customer_menu(self, username):
        while True:
            os.system('cls')
            print('''
            ================================================
            ||              CUSTOMER MENU                 ||
            ================================================
            1. Lihat Barang
            2. Beli Barang
            3. Top-Up saldo
            4. Keluar
            ================================================
            ''')
            choice = input("Pilih menu: ")
            if choice == '1':
                self.barang.display()
            elif choice == '2':
                self.pembelian_customer(username)
            elif choice == '3':
                self.top_up_saldo(username)
            elif choice == '4':
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

                choice = input("Pilih menu: ")
                if choice == '1':
                    if self.login_admin():
                        self.admin_menu()
                    else:
                        print("Autentikasi gagal. Username atau password salah.")
                elif choice == '2':
                        username = self.login_customer()
                        if username:
                            self.customer_menu(username)
                        else:
                            print("Autentikasi gagal. Username atau password salah.")
                elif choice == '3':
                        username = input("Username: ")
                        password = input("Password: ")
                        saldo = int(input("Saldo e-money: "))
                        self.tambah_customer(username, password, saldo)  # Perubahan di sini
                        print("Customer berhasil didaftarkan.")
                elif choice == '4':
                        print("Terima kasih telah menggunakan aplikasi kami.")
                        break
                else:
                    print("Pilihan tidak valid.")
                    input("Tekan Enter untuk melanjutkan...")

            except ValueError as rawr:
                print("ERROR ON APLIKASI BRO", rawr)


app = CHIPIStore()
app.main()

