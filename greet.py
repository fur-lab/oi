import os

# Admin
def greet_admin(Nama):

    os.system("cls")
    print(f"Selamat datang admin {Nama}")
    print("="*75)
    input("Tekan ENTER untuk lanjut ke menu admin...")

# Pelanggan
def greet_pelanggan(nama_pengunjung):
    
    os.system("cls")
    print(f"Selamat datang {nama_pengunjung}")
    print("="*75)
    input("Tekan ENTER untuk lanjut ke menu...")
