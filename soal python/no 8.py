print("="*25)
print("PROGRAM TABUNG")
print("="*25)

PHI = 3.14
PHI2 = 22/7

jari = float(input("masukan nilai jari jarinya :"))
tinggi = float(input("masukan nilai tingginya :"))

if jari % 2 == 0 :
    volume = 2 * PHI * jari * tinggi
    luas = (PHI * jari**2) + (2 * PHI * jari * tinggi)

    print (f"""
volume tabung : {volume} cm3
luas permukaan : {luas} cm2

""")
    
else :
    volume = 2 * PHI2 * jari * tinggi
    luas = (PHI2 * jari**2) + (2 * PHI2 * jari * tinggi)

    print (f"""
volume tabung : {volume} cm3
luas permukaan : {luas} cm2

""")