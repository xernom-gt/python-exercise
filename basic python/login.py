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

    else :
        print ("username atau password salah ")
