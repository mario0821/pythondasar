# Input tinggi segitiga dari pengguna
tinggi = int(input("Masukkan tinggi segitiga: "))

# Perulangan untuk mencetak setiap baris segitiga
for i in range(1, tinggi + 1):
    # Mencetak spasi sebelum karakter "*"
    for j in range(tinggi - i):
        print(" ", end="")
    
    # Mencetak karakter "*" sesuai dengan nomor baris
    for k in range(2 * i - 1):
        print("*", end="")
    
    # Pindah ke baris berikutnya
    print()