skor = int(input("Masukkan skor siswa: "))

if skor >= 75:
  print("Siswa lulus")
else:
  ulang = input("Apakah siswa ingin mengulang tes? (y/n): ")
  if ulang == "y":
    print("Siswa mengulang tes")
  else:
    print("Siswa gagal")