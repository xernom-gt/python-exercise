text = input("Masukkan string: ")
contains_digit = any(char.isdigit() for char in text)
print("String mengandung angka:", contains_digit)
