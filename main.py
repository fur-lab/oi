# Berisi program utama 
from func import *
from data import *
from greet import *
from admin import *
from user import *

import os
import time
from prettytable import PrettyTable

while True :

    loading()
    tampilkan_header_utama()
    menu_awal()

    pilihan_utama = input("Pilih menu (1-3): ")

    if pilihan_utama == "1":
                layar_bersih()
                login()
                pilihan_login = input("Pilih menu (1-2): ")

                if pilihan_login == "1" : # Login Admin
                    layar_bersih()
                    tampilkan_header_utama()
                
                    while percobaan < max_percobaan:
                            Login_Username = input("Masukkan username Admin : ")
                            Login_Password = input("Masukan password Admin : ")


                            if Login_Username == Username and Login_Password == Password  :
                
                                Admin = True
                                status_login = True
                                break
                                    

                            else:
                                percobaan += 1
                                print("Username atau Password salah !!!")
                                layar_bersih()

                                if percobaan == max_percobaan :
                                    layar_bersih()
                                    print("Username atau Password salah !!!")
                                    input("Tekan Enter untuk memulai dari awal......")
                                    break
                    
                if pilihan_login == "2" : # Login User
                    layar_bersih()
                    tampilkan_header_utama()

                    while percobaan < max_percobaan:
                        Login_Username = input("Masukkan username : ")
                        Login_Password = input("Masukan password : ")


                        if Login_Username == pengguna and Login_Password == Password  :
            
                            User = True
                            status_login = True
                            break
                                

                        else:
                            percobaan += 1
                            print("Username atau Password salah !!!")
                            layar_bersih()

                            if percobaan == max_percobaan :
                                layar_bersih()
                                print("Username atau Password salah !!!")
                                input("Tekan Enter untuk memulai dari awal......")
                                break

                while Admin == True :
                    while status_login == True:
                        layar_bersih()
                        menu_admin()

                        pilihan_admin = input("Pilih menu (1-6): ")

                        if pilihan_admin == "1":   # Lihat menu
                            layar_bersih()
                            tampilkan_daftar_produk() # ini pakai prosedur 1
                        
                        elif pilihan_admin == "2":   # Update
                            layar_bersih()
                            update()
                        
                        elif pilihan_admin == "3":   # Edit
                            layar_bersih()
                            edit()

                        elif pilihan_admin == "4":   # Edit
                            layar_bersih()
                            hapus()
                        
                        elif pilihan_admin == "5":   # Cari
                            layar_bersih()
                            print("=" * 59)
                            print("|                      CARI PRODUK                        |")
                            print("=" * 59)
                            keyword = input("Masukkan nama produk: ")
                            
                            cari_produk_dan_tampilkan(keyword)
                            
                        elif pilihan_admin == "6":
                                layar_bersih()
                                print("Logout berhasil!")
                                Admin = False
                                status_login = False
                        
                        else:
                            print("Pilihan tidak valid!")
                    
                while User == True :
                    while status_login == True:
                        layar_bersih()
                        menu_user()
                        
                        pilihan_user = input("Pilih menu (1-7): ")
                        
                        # fitur buat lihat produk
                        if pilihan_user == "1":
                            layar_bersih()
                            tampilkan_daftar_produk() #ini pakai prosedur 1
                            time.sleep(7)

                        # fitur buat mempermudah cari produk
                        elif pilihan_user == "2":
                            layar_bersih()
                            print("=" * 50)
                            print("|                  CARI PRODUK                   |")
                            print("=" * 50)
                            keyword = input("Masukkan nama produk: ")
                            
                            cari_produk_dan_tampilkan(keyword)
                            time.sleep(5)

                        # fitur tambahkan produk ke keranjang
                        elif pilihan_user == "3":
                            layar_bersih()
                            tambah_keranjang ()

                        # fitur lihat keranjang
                        elif pilihan_user == "4":
                            layar_bersih()
                            tampilkan_isi_keranjang(user_login) #ini pakai prosedur 2
                            time.sleep(7)
                        
                        # fitur hapus dari keranjang
                        elif pilihan_user == "5":
                            layar_bersih()
                            hapus_keranjang()
                        
                        # fitur logout
                        elif pilihan_user == "7":
                            print("Logout berhasil!")
                            time.sleep(4)
                            status_login = False
                        
                        else:
                            print("Pilihan tidak valid!")
                            time.sleep(4)


                    
    elif pilihan_utama == "2":
        layar_bersih()
        tampilkan_header_utama()
        register()
    
    elif pilihan_utama == "3":
        layar_bersih()
        print("Terima kasih telah mengunjungi Toko Peralatan Kucing Wingky!")
        break
    
    else:
        print("Pilihan tidak valid!")