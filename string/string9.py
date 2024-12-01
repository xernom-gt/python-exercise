
status_lampu = input('Status Lampu :').lower
warna_lampu = input('Warna Lampu  :').lower

if status_lampu == 'menyala' : 
    if warna_lampu == 'merah' :
        print('BERHENTI')
    elif warna_lampu == 'kuning' :
        print('BERSIAP')
    elif warna_lampu == 'hijau' :
        print('JALAN')
    else :
        print('gda apa apa')
else :
    print('EROR --')