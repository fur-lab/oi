# Berisi Kumpulan fungsi dan logika dari program
import os
import time
from prettytable import PrettyTable
import pwinput
#Import semua data dari Data.py
from data import pengguna, produk, keranjang, user_login, role_login, status_login, KATEGORI_VALID


# FUNGSI UMUM
def layar_bersih():
    os.system("cls")

def loading(lama = 30, waktu = 2.5):
    for i in range(lama + 1):
        time.sleep(waktu / lama)  
        bar = "=" * i + "-" * (lama - i)  
        print(f"\rLoading: [{bar}] {i * 100 // lama}%", end="")
    layar_bersih()
    print("Berhasil memuat.....")
    input("Tekan ENTER untuk lanjut ke menu...")
    layar_bersih()

def main():
    global user_login, role_login, status_login

##### TAMPILAN AWAL #####
def menu_awal():
    print("1. Login")
    print("2. Register")
    print("3. Keluar")

def login() :
        print("=" * 50)
        print(f"|               MENU LOGIN              |")
        print("=" * 50)
        print("1. Admin")
        print("2. User")
        

def register () :
        print("\n-------------------- REGISTER SECTION ----------------------")
        
        try:
            username_baru = input("Username baru: ")
            if not username_baru:
                raise ValueError("Username tidak boleh kosong")
            
            if username_baru in pengguna:
                raise ValueError("Username sudah terdaftar!")
            
            password_baru = pwinput.pwinput(prompt="Silahkan input password baru: ", mask="*") # Menggunakan passwordnya
            if not password_baru:
                raise ValueError("Password tidak boleh kosong")
            
            pengguna[username_baru] = {
                "password": password_baru,
                "role": "user"
            }
            
            print(f"\nRegistrasi berhasil! Silakan login dengan username '{username_baru}'")
            time.sleep(4)
            
        except ValueError as e:
            print(f"\nError: {e}")
            time.sleep(4)





# Fungsi 1 yang pakai parameter
def validasi_input_angka(prompt, pesan_error="Input harus berupa angka!"):
    while True:
        try:
            input_str = input(prompt) #ini variabel lokal 
            if not input_str:
                return None
            hasil = int(input_str) #ini variabel lokal 
            return hasil
        except ValueError:
            print(f"\n{pesan_error}")
            time.sleep(4)
            return None

# Fungsi ke 2 yang pakai parameter juga
def hitung_total_keranjang_rekursif(list_items, index=0):
    if index >= len(list_items): #base case
        return 0
    
    item_sekarang = list_items[index]
    subtotal = item_sekarang["harga"] * item_sekarang["jumlah"]
    return subtotal + hitung_total_keranjang_rekursif(list_items, index + 1) #fungsi rekursif

# Fungsi 1 yang gaada parameternya
def tampilkan_header_utama():
    print("=" * 60)
    print("|      SELAMAT DATANG DI TOKO PERALATAN KUCING WINGKY      |")
    print("=" * 60)

# Fungsi ke 2 yang gaada parameternya
def generate_id_produk_baru():
    if len(produk) == 0:
        id_baru = 1
    else:
        id_baru = max(produk.keys()) + 1
    return id_baru

def tampilkan_daftar_produk(): #prosedur 1
    print("\n" + "=" * 59)
    print("|                   DAFTAR PRODUK WINGKY                  |")
    print("=" * 59)
    
    if len(produk) == 0:
        print("Tidak ada produk tersedia.")
    else:
        table = PrettyTable()
        table.field_names = ["ID", "Nama Produk", "Kategori", "Harga", "Stok"]
        table.align["ID"] = "c"
        table.align["Nama Produk"] = "l"
        table.align["Kategori"] = "l"
        table.align["Harga"] = "r"
        table.align["Stok"] = "c"
        
        for id_produk, data in produk.items(): #ini variabel lokal yang ada dalam loop
            table.add_row([
                id_produk,
                data['nama'],
                data['kategori'],
                f"Rp {data['harga']:,}",
                data['stok']
            ])
        
        print(table)
    
    print("=" * 59)

def tampilkan_isi_keranjang(current_user): #prosedur ke 2
    global keranjang
    
    print("=" * 59)
    print("|                   KERANJANG BELANJA                     |")
    print("=" * 59)
    
    if current_user not in keranjang or len(keranjang[current_user]) == 0:
        print("\nKeranjang belanja kosong.")
        print("=" * 59)
        return 0
    else:
        table = PrettyTable()
        table.field_names = ["No", "Nama Produk", "Harga", "Jumlah", "Subtotal"]
        table.align["No"] = "c"
        table.align["Nama Produk"] = "l"
        table.align["Harga"] = "r"
        table.align["Jumlah"] = "c"
        table.align["Subtotal"] = "r"
        
        nomor = 1 #ini variabel lokal 
        list_items = [] #ini variabel lokal 
        
        for id_produk, item in keranjang[current_user].items(): #ini ada pakai variabel lokal 
            subtotal = item["harga"] * item["jumlah"] #ini ada pakai variabel lokal 
            list_items.append(item)
            table.add_row([
                nomor,
                item['nama'],
                f"Rp {item['harga']:,}",
                item['jumlah'],
                f"Rp {subtotal:,}"
            ])
            nomor += 1
        
        print(table)
        
        #fungsi rekursif untuk hitung total
        total = hitung_total_keranjang_rekursif(list_items) #ini ada pakai variabel lokal 
        
        print(f"{'TOTAL':>10} Rp {total:,}")
        print("=" * 59)
        return total

# Fungsi khusus untuk pencarian produk (fitur buat mempermudah cari produk)
def cari_produk_dan_tampilkan(keyword):
    print("\n" + "=" * 59)
    print("|                     HASIL PENCARIAN                     |")
    print("=" * 59)
    
    # Menggunakan PrettyTable untuk menampilkan hasil pencarian
    table = PrettyTable()
    table.field_names = ["ID", "Nama Produk", "Kategori", "Harga", "Stok"]
    table.align["ID"] = "c"
    table.align["Nama Produk"] = "l"
    table.align["Kategori"] = "l"
    table.align["Harga"] = "r"
    table.align["Stok"] = "c"
    
    ketemu = False
    for id_produk, data in produk.items():
        if keyword.lower() in data['nama'].lower():
            table.add_row([
                id_produk,
                data['nama'],
                data['kategori'],
                f"Rp {data['harga']:,}",
                data['stok']
            ])
            ketemu = True
    
    if ketemu:
        print(table)
    else:
        print("\nProduk tidak ditemukan.")
    print("=" * 59)