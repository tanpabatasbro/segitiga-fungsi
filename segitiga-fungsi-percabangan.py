import math # math module

def menuAwal():
    pilihMenu = int(input("\nMAU NYARI APA BRO ? \n 1. Sisi miring segitiga \n 2. Tinggi segitiga \n 3. Alas segitiga \n 4. Keluar\n Masukkan Pilihan (1/2/3/4): "))
    
    if pilihMenu == 1:
        sisiMiringSegitiga()
    elif pilihMenu == 2:
        tinggiSegitiga()
    elif pilihMenu == 3:
        alasSegitiga()
    else:
        keluarProgram()
        
def sisiMiringSegitiga():
    alas = int(input("\nMasukkan Nilai Alas segitiga : "))
    tinggi = int(input("\nMasukkan Nilai Tinggi Segitiga : "))    
    hitungSisiMiring = int(math.sqrt(tinggi **2 + alas **2))
    print(f"Sisi Miring segitiga = {hitungSisiMiring}")
    menuAwal()
    
def tinggiSegitiga():
    sisi = int(input("\nMasukkan Nilai Sisi Miring Segitiga : "))
    alas = int(input("\nMasukkan Nilai Alas Segitiga : "))
    hitungTinggiSegitiga = int(math.sqrt(sisi **2 - alas **2))
    print(f"\nTinggi segitiga = {hitungTinggiSegitiga}")
    menuAwal()
    
def alasSegitiga():
    tinggi = int(input("\nMasukkan Nilai Tinggi segitiga : "))
    sisi = int(input("\nMasukkan Nilai Sisi Miring segitiga : "))
    hitungAlasSegitiga = int(math.sqrt(sisi **2 - tinggi **2))
    print(f"\nAlas segitiga = {hitungAlasSegitiga}")
    menuAwal()
def keluarProgram():
    print("\n--->>>>>TERIMA KASIH<<<<<---\n")
    
menuAwal()