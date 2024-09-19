nama = input('MASUKAN NAMA ANDA :')
data = int(input('MASUKAN NILAI ANDA :'))

if data >= 75 and data <= 100 :
    print (f'SELAMAT ANANDA {nama} !! \nANDA DINYATAKAN LULUS DENGAN NILAI YANG DI PEROLEH {data} ')

elif data <= 75 : 
    print (f'MAAF ANANDA {nama} \n ANDA DINYATAKAN TIDAK LULUS DENGAN NILAI YANG DI PEROLEH {data}')

else :
    print ('MAAF NILAI TIDAK VALID')