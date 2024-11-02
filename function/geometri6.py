def data():
    print ("volume bola")
    jari = int(input("masukan jari jarinya :"))

    if jari % 2 :
        volume = lambda : (4/3) *3.14* jari ** 3
        print(f'volume bola adalah {int(volume())} cm3') 
    else : 
        volume = lambda : (4/3) *22/7* jari ** 3
        print(f'volume bola adalah {int(volume())} cm3') 
data()