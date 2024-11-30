teks = input("Masukkan sebuah kalimat atau kata: ")

vokal = "aeiouAEIOU"

jumlah_vokal = sum(1 for huruf in teks if huruf in vokal)

print(f"Jumlah huruf vokal dalam string adalah: {jumlah_vokal}")
