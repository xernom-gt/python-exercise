import random

def tebak_tebakan():
    tebak_tebakan_list = [
        {"jawaban" : "3"},
        {"jawaban" : "1"},
        {"jawaban" : "2"}
    ]

    print ("=== selamat datang dan silahkan menebak ===\n")

    jawab = random.choice(tebak_tebakan_list)["jawaban"]

    tebak = input("coba tebak angka diantara 1 sampai 3 ada di mana si alucard :")

    if tebak == jawab:
        print ("selamat!! kamu benar  🎉")

    else :
        print (f"tetotttt!! kamu salah jawaban yang benar adalah {jawab}")

tebak_tebakan()