# Input tinggi segitiga dari pengguna
tinggi = int(input("Masukkan tinggi segitiga: "))

# Perulangan untuk mencetak setiap baris segitiga
for i in range(1, tinggi + 1):
    # Mencetak karakter "*" sesuai dengan nomor baris
    for j in range(i):
        print("*", end="")
    
    # Pindah ke baris berikutnya
    print()