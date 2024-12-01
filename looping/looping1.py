account = "user"
password = "12345"

login = input("sudah punya akun ? n/y :")

if login == "n" :
    account = input("masukan nickname :")
    password = input ("masukan password :")
    print ("akun berhasil di buat silahkan login ulang")

if login == "y" or login == "n" :
    login = input ("masukan username :")
    password1 = input ("masukan password :")

    if login == account and password1 == password :
        print (f"selamat datang {account}!")
        while True :

            print ("""
                    silahkan pilih opsi
                    1. mengecek akun
                    2. ganti password
                    3. ganti username
                    4. exit
                    """)
            choice = input ("silahkan pilih opsi :")
            if choice == "1" :
                print (f"""
                       username: {account}
                       password: {password}
                       """)
            elif choice == "2" :
                password = input ("masukan password baru :")
                print ("password berhasil di ubah!!")
            
            elif choice == "3" :
                account = input ("masukan username baru :")
                print ("username berhasil di ubah!!")
            
            elif choice == "4" :
                print ("terima kasih")
                break

            else :
                print ("inputan invalid")
            print (" " + "="*40 + " ")
    else :
        print ("username atau password salah ")