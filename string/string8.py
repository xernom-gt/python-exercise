tabungan = 400000000

while True :
    menu = (input("""
        silah kan memilih opsi
        1.nabung        2.tarik uang
        3.transfer      4.cek nominal
        5.exit             
        
        :"""))

    if menu == "1":
        nab = int(input("masukan nominal :"))
        print (f"selamat saldo anda berhasil ditambahkan!!")

    elif menu == "2":
        tarik = int(input("masukan nominal :"))
        print (f"berhasil menarik dari saldo anda")

    elif menu == "3":
        rek = input("silahkan pilih no tujuan :")
        tar = int(input("masukan nominal :"))
        tabungan -= tar
        print (f"selamat transfer berhasil ke no rekening {rek}")


    elif menu == "4":
        print (f"tabungan anda \t {tabungan}")
    
    elif menu == "5" :
        print ("terima kasih!!")
        break

    else : 
        print ("tidak valid harap ulang kembali")