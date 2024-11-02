def data():
    print("volume prisma segitiga")
    alas = int(input("masukan nilai alasnya :"))
    tinggi = int(input("masukan nilai tingginya :"))
    tinggiP = int(input("masukan nilai tinggi prismanya :"))
    volume = lambda : (alas * tinggi) / 2 * tinggiP
    print (f"volume prisma segitiga adalah {volume()} cm3")
data()
data()
data()