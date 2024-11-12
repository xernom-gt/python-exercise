def data():
    print("="*35)
    print("\t volume prisma segiempat")
    print("="*35)

    la = int(input('masukan nilai luas alas nya :'))
    t = int(input('masukan nilai tinggi nya :'))
    
    jum = lambda : 1/3 * la * t
    print (f'volume prisma segiempat adalah {int(jum())} cm3')

data()
data()
data()