nilai = float(input("masukan nilai anda :"))

if nilai > 100 :
    print("nilai anda tidak valid")

elif nilai >= 90 or nilai == 100 :
    print("anda GRADE A")

elif nilai >= 80 or nilai == 89 :
    print ("anda GRADE B")

elif nilai >= 70 or nilai == 79 :
    print ("anda GRADE c")
    
else :
    print ("anda GRADE E")
