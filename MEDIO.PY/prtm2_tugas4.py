import math

class Shape:
    def hitunng_luas(self):
        pass

class Square(Shape):
    def init(self, sisi):
        self.sisi = sisi

    def hitung_luas(self):
        return self.sisi ** 2
    
class Circle(Shape):
    def init(self, radius):
        self.radius = radius

    def hitunng_luas(self):
        return math.pi * self.radius ** 2
    
class Triangle(Shape):
    def init(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def hitunng_luas(self):
        return 0.5 * self.alas * self.tinggi
    
if __name__ == "_main_":
    bentuk1 = Square(5)
    bentuk2 = Circle(3)
    bentuk3 = Triangle(4, 6)

    daftar_bentuk = [bentuk1, bentuk2, bentuk3]

    for bentuk in daftar_bentuk:
        luas = bentuk.hitung_luas()
        if isinstance(bentuk, Square):
            print(f"Luas Persegi: {luas}")
        elif isinstance(bentuk, Circle):
            print(f"Luas Lingkaran: {luas}")
        elif isinstance(bentuk, Triangle):
            print(f"Luas Segitiga: {luas}")