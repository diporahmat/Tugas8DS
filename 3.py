import os
import platform

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def konversi_grade(nilai):
    if 90 <= nilai <= 100:
        return 'A'
    elif 85 <= nilai < 90:
        return 'A-'
    elif 80 <= nilai < 85:
        return 'B+'
    elif 75 <= nilai < 80:
        return 'B'
    elif 70 <= nilai < 75:
        return 'B-'
    elif 65 <= nilai < 70:
        return 'C+'
    elif 60 <= nilai < 65:
        return 'C'
    elif 50 <= nilai < 60:
        return 'D'
    elif 40 <= nilai < 50:
        return 'E'
    else:
        return 'T'

def hitung_nilai_akhir(tugas, uts, uas):
    return 0.30 * tugas + 0.30 * uts + 0.40 * uas

def main():
    while True:
        clear_screen() 
        
        data_mahasiswa = []
        total_nilai = 0
        
        jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))

        for i in range(jumlah_mahasiswa):
            NIM = input("\nMasukkan NIM: ")
            Nama = input("Masukkan Nama: ")
            Nilai_Tugas = float(input("Masukkan Nilai Tugas: "))
            UTS = float(input("Masukkan Nilai UTS: "))
            UAS = float(input("Masukkan Nilai UAS: "))

            nilai_akhir = hitung_nilai_akhir(Nilai_Tugas, UTS, UAS)
            grade = konversi_grade(nilai_akhir)

            mahasiswa = {
                "NIM": NIM,
                "Nama": Nama,
                "Nilai Tugas": Nilai_Tugas,
                "UTS": UTS,
                "UAS": UAS,
                "Nilai Akhir": nilai_akhir,
                "Grade": grade
            }
            data_mahasiswa.append(mahasiswa)
            total_nilai += nilai_akhir

        print("\nLaporan Nilai Data Science")
        print(f"{'No.':<4} | {'NIM':<10} | {'Nama':<10} | {'TGS':<4} | {'UTS':<4} | {'UAS':<4} | {'Akhir':<5} | {'Grade':<5}")
        print("-" * 66)
        for idx, mhs in enumerate(data_mahasiswa, 1):
            print(f"{idx:<4} | {mhs['NIM']:<10} | {mhs['Nama']:<10} | {mhs['Nilai Tugas']:<4} | {mhs['UTS']:<4} | {mhs['UAS']:<4} | {mhs['Nilai Akhir']:5.2f} | {mhs['Grade']:<5}")

        nilai_tertinggi = max(data_mahasiswa, key=lambda x: x['Nilai Akhir'])
        nilai_terendah = min(data_mahasiswa, key=lambda x: x['Nilai Akhir'])
        rata_rata = total_nilai / len(data_mahasiswa)

        print("-" * 66)
        print(f"Total Nilai: {total_nilai:.2f}")
        print(f"Nilai Rata-rata: {rata_rata:.2f}")
        print(f"Nilai Terendah: {nilai_terendah['Nilai Akhir']:5.2f}, NIM: {nilai_terendah['NIM']} - Nama: {nilai_terendah['Nama']}")
        print(f"Nilai Tertinggi: {nilai_tertinggi['Nilai Akhir']:5.2f}, NIM: {nilai_tertinggi['NIM']} - Nama: {nilai_tertinggi['Nama']}")

        # Tanya pengguna apakah ingin mengulang keseluruhan program
        ulang_program = input("\nApakah Anda ingin mengulang keseluruhan program? (y/n): ")
        if ulang_program.lower() != 'y':
            print("Program selesai.")
            break

if __name__ == "__main__":
    main()