user = input("Menginput [tabung,balok]:")

if user == "tabung" :
    phi = 3.14
    r = int (input("masukkan r : "))
    t = int (input("masukkan t : "))
    volume = phi * r * r * t
    print ("volume",volume)

elif user == "balok" :
    panjang = int (input("masukkan panjang : "))
    lebar = int (input("masukkan lebar : "))
    tinggi = int (input("masukkan tinggi : "))
    volume = panjang * lebar * tinggi
    print ("volume",volume)