def data():
    print ("menghitung volume tabung")
    phi = 22/7
    phi2 = 3.14
    
    jari = int(input("masukan jari jari nya:"))
    tinggi = int(input("masukan tingginya :"))

    if jari % 2 :
        jumlah = lambda: phi2 * jari ** 2
        print (f"volume tabung adalah {jumlah()}cm3")
    else :
        jumlah = lambda :  phi * jari ** 2 
        print (f"volume tabung adalah {jumlah()}cm3")
data()
data()
data()