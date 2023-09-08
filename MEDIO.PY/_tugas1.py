user = input ("Menghitung [persegi/persegi panjang/trapesium,]:")

if user == "persegi" :
    sisi = int (input("masukkan sisi : "))
    keliling  = 4 * sisi
    luas = sisi * sisi
    print ("keliling",keliling)
    print ("luas",luas)

elif user == "persegi panjang" :
    panjang = int (input("masukkan panjang : "))
    lebar = int (input("masukkan lebar : "))
    keliling  = 2 * (panjang + lebar)
    luas = panjang * lebar
    print ("keliling",keliling)
    print ("luas",luas)

elif user == "trapesium" :
    a = int (input("masukkan a : "))
    b = int (input("masukkan b : "))
    tinggi  = int (input("masukkan tinggi : "))
    m1 = int (input("masukkan m1 : "))
    m2 = int (input("masukkan m2 : "))
    keliling  = a + b + m1 + m2
    luas = ((a+b) * tinggi ) / 2
    print ("keliling",keliling)
    print ("luas",luas)


