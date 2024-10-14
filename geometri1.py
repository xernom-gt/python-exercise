# def persegi():
#     sisi = int (input('sisi\t\t\:'))
#     luas = lambda s: s*s 
#     keliling = lambda s: 4*s
    

def data():
    phi = 22/7
    phi2 = 3.14
    r = int(input('masukan jari jari :'))
    t = int(input('masukan tingginya :'))

    if r % 2 :
        v = lambda :phi * (r*r) * t
        print('volumenya adalah',int(v()))

    else :
        v = lambda :phi2 * (r*r) * t
        print('volumenya adalah',int(v()))
data()
data()
data()  