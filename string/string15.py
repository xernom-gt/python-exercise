text = input("kata kata hari ini : ")

doubled_text = ''.join(char * 2 for char in text)

print(f"Teks doksli: {text}")
print(f"Teks setelah huruf digandakan: {doubled_text}")
