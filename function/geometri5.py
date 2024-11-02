def data():
    print("volume persegi panjang")
    panjang = int(input("masukan panjangnya :"))
    lebar = int(input("masukan lebarnya :"))
    tinggi = int(input("masukan tinggignya :"))

    volume = lambda : panjang * lebar * tinggi

    print(f"volume persegi panjang adalah {volume()} cm3")
data()
data()
data()