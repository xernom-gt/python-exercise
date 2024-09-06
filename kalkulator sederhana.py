nilai1 = int(input('MASUKAN NILAI PERTAMA :'))
nilai2 = int(input('MASUKAN NILAI KEDUA :'))
sistem = input('SILAHKAN SISTEM OPERASI BERIKUT ==> +,/,-,* :')

if sistem == '+' :
    hasil = nilai1 + nilai2
    print (hasil)

elif sistem == '*' :
    hasil = nilai1 * nilai2
    print (int(hasil))

elif sistem == '-' :
    hasil = nilai1 + nilai2
    print (hasil)

elif sistem == '/' :
    hasil = nilai1 / nilai2
    print (int(hasil))

else :
    print ('MAAF SISTEM OPERASI SALAH SILAHKAN ULANGI')