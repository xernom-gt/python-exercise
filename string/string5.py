text = input("Masukkan string: ")
print("String adalah angka negatif:", text.startswith('-') and text[1:].isdigit())
