kamus_warna = {
    "red": "merah",
    "blue": "biru",
    "green": "hijau",
    "yellow": "kuning",
    "black": "hitam",
    "white": "putih",
    "purple": "ungu",
    "orange": "jingga",
    "pink": "merah muda",
    "gray": "abu-abu",
    "brown": "cokelat"
}

def translator():
    while True :
        print ("""
        Program Mentrasnlatekan warna
        Pilih opsi 
        1. Trasnlate dari inggris ke indonesia 
        2. translate dari indonesia ke inggris
        3. exit
        """)

        pil = input("Masukan pilihan anda (1/2/3) :")

        if pil == "1" :
            warna_inggris = input("Masukan nama warna dalam bahasa inggris :")
            hasil = kamus_warna.get(warna_inggris), "warna tidak di temukan dalam kamus"
            print (f"Warna dalam bahasa indonesia: {hasil}")
        
        elif pil == "2":
            warna_indonesia = input("Masukan warna dalam bahasa indonesia :")
            kamus_terbalik = {v: k for k, v in kamus_warna.items()}
            hasil = kamus_terbalik.get(warna_indonesia, "Warna tidak ditemukan dalam kamus.")
            print(f"Warna dalam bahasa Inggris: {hasil}")

        elif pil == "3" :
            print ("terima kasih sampai jumpah")
            break
        
        else :
            print ("pilihan tidak valid silahkan coba lagi")

        print ("\n" + "="*40 + "\n")
translator()