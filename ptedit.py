# Berisi program utama 
from func import *
from data import *
from greet import *
from admin import *
from user import *

import os
import time
import pwinput 
from prettytable import PrettyTable

def main():
    global user_login, role_login, status_login
    
    while True: #program utamanya
        loading()
        tampilkan_header_utama() #ini pakai fungsi 1
        menu_awal()
            
        pilihan_utama = input("\nPilih menu (1-3): ")
        
        # Menu login
        if pilihan_utama == "1":
            tampilkan_header_utama() # ini pakai fungsi 1
            print("\n-------------------- LOGIN SECTION -------------------------")

            try: # Error handling untuk bagian login
                username = input("Username: ") #ini variabel lokal 
                if not username:
                    raise ValueError("Username tidak boleh kosong")
                
                password = pwinput.pwinput(prompt="Password: ", mask="*") #ini variabel lokal - menggunakan pwinput
                if not password:
                    raise ValueError("Password tidak boleh kosong")
                
                # Verifikasi login dulu disini
                if username in pengguna and pengguna[username]["password"] == password:
                    user_login = username
                    role_login = pengguna[username]["role"]
                    status_login = True
                    print(f"\nLogin berhasil! Selamat datang, {user_login}")
                    time.sleep(4)
                    
                    # Menu adminnya
                    if role_login == "admin":
                        while status_login == True:
                            os.system('cls || clear')
                            menu_admin()

                            
                            pilihan_admin = input("\nPilih menu (1-6): ")
                            
                            # fitur lihat produk
                            if pilihan_admin == "1":
                                os.system('cls || clear')
                                tampilkan_daftar_produk() # ini pakai prosedur 1
                                time.sleep(10)
                            
                            # fitur tambah produk
                            elif pilihan_admin == "2":
                                os.system('cls || clear')

                                update()
                                
                                
                            # fitur update produknya
                            elif pilihan_admin == "3":
                                os.system('cls || clear')

                                edit()
                                    
                                
                                
                            # fitur hapus produk
                            elif pilihan_admin == "4":
                                os.system('cls || clear')

                                hapus()
                            
                            # fitur buat mempermudah cari produk 
                            elif pilihan_admin == "5":
                                os.system('cls || clear')
                                print("=" * 59)
                                print("|                      CARI PRODUK                        |")
                                print("=" * 59)
                                keyword = input("\nMasukkan nama produk: ")
                                
                                cari_produk_dan_tampilkan(keyword)
                                time.sleep(4)
                            
                            # fitur buat log out
                            elif pilihan_admin == "6":
                                print("\nLogout berhasil!")
                                time.sleep(4)
                                status_login = False
                            
                            else:
                                print("\nPilihan tidak valid!")
                                time.sleep(4)
                    
                    # menu pengguna
                    else:
                        while status_login == True:
                            os.system('cls || clear')
                            menu_user()
                            
                            pilihan_user = input("\nPilih menu (1-7): ")
                            
                            # fitur buat lihat produk
                            if pilihan_user == "1":
                                os.system('cls || clear')
                                tampilkan_daftar_produk() #ini pakai prosedur 1
                                time.sleep(7)

                            # fitur buat mempermudah cari produk
                            elif pilihan_user == "2":
                                os.system('cls || clear')
                                print("=" * 50)
                                print("|                  CARI PRODUK                   |")
                                print("=" * 50)
                                keyword = input("\nMasukkan nama produk: ")
                                
                                cari_produk_dan_tampilkan(keyword)
                                time.sleep(5)

                            # fitur tambahkan produk ke keranjang
                            elif pilihan_user == "3":
                                os.system('cls || clear')
                                tambah_keranjang ()
                                
                            # fitur lihat keranjang
                            elif pilihan_user == "4":
                                os.system('cls || clear')
                                tampilkan_isi_keranjang(user_login) #ini pakai prosedur 2
                                time.sleep(7)

                            # fitur hapus dari keranjang
                            elif pilihan_user == "5":
                                os.system('cls || clear')
                                hapus_keranjang()
                            
                            # fitur checkout
                            elif pilihan_user == "6":
                                os.system('cls || clear')
                                checkout() 
                                

                            # fitur logout
                            elif pilihan_user == "7":
                                print("\nLogout berhasil!")
                                time.sleep(4)
                                status_login = False
                            
                            else:
                                print("\nPilihan tidak valid!")
                                time.sleep(4)
                else:
                    print("\nUsername atau password salah!")
                    time.sleep(4)
                    
            except ValueError as e:
                print(f"\nError: {e}")
                time.sleep(4)
        
        # Menu Register
        elif pilihan_utama == "2":
            tampilkan_header_utama()
            register()

        # Menu Keluar
        elif pilihan_utama == "3":
            print("Terima kasih telah mengunjungi Toko Peralatan Kucing Wingky!")
            break
        
        else:
            print("Pilihan tidak valid!")
            time.sleep(4)

if __name__ == "__main__":
    main()
