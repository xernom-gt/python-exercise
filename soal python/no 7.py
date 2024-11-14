print("="*25)
print("PROGRAM LINGKARAN")
print("="*25)
PHI = 3.14
PHI2 = 22/7

jari_jari = float(input("masukan jari jari nya :"))

if jari_jari % 2 == 0 :
    luas = PHI * jari_jari**2 
    keliling = PHI * 2 * jari_jari

    print (f"""
        Luas : {luas} cm2
        Keliling : {keliling} cm
            """)
    
else :

    luas = PHI2 * jari_jari**2 
    keliling = PHI2 * 2 * jari_jari

    print (f"""
        Luas : {luas} cm2
        Keliling : {keliling} cm
            """)