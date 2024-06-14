import os
import platform

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def hitung_total(biaya_layanan, lama_member):
    if lama_member >= 20:
        diskon = 0.15
    elif lama_member >= 10:
        diskon = 0.10
    elif lama_member >= 5:
        diskon = 0.05
    else:
        diskon = 0.00
    
    jumlah_diskon = diskon * biaya_layanan
    total = biaya_layanan - jumlah_diskon
    return total, jumlah_diskon

def main():
    while True:
        clear_screen()

        kode_member = input("Masukkan kode member: ")
        nama_member = input("Masukkan nama member: ")
        biaya_layanan = float(input("Masukkan biaya layanan: "))
        lama_member = int(input("Masukkan lama menjadi member (tahun): "))

        total, jumlah_diskon = hitung_total(biaya_layanan, lama_member)
        
        print("\nOutput:")
        print(f"Kode Member: {kode_member}")
        print(f"Nama Member: {nama_member}")
        print(f"Biaya Layanan: Rp{biaya_layanan:,.2f}")
        print(f"Lama Menjadi Member: {lama_member} tahun")
        print(f"Total Bayar Setelah Diskon: Rp{total:,.2f}")

        response = input("\nApakah Anda ingin mengulang? (y/n): ")
        if response.lower() != 'y':
            print("Program selesai.")
            break

if __name__ == "__main__":
    main()
