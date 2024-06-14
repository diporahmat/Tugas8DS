import os
import platform

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def search_nilai_tengah(angka):
    angka.sort()
    return angka[1]

while True:

    clear_screen()

    angka = []

    print("Masukkan tiga bilangan bulat yang berbeda:")
    for i in range(3):
        while True:
            try:
                num = int(input(f"Masukkan bilangan {i+1}: "))
                if num not in angka:
                    angka.append(num)
                    break
                else:
                    print("Bilangan sudah dimasukkan, silakan masukkan bilangan yang berbeda.")
            except ValueError:
                print("Masukkan nilai berupa bilangan bulat.")

    nilai_tengah = search_nilai_tengah(angka)
    print("Bilangan dengan nilai tengah adalah:", nilai_tengah)

    response = input("Apakah Anda ingin mengulang? (y/n): ")
    if response.lower() != 'y':
        print("Program selesai.")
        break
