num = int(input("Masukkan angka: "))
is_prime = True
for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break
print("Bilangan prima" if is_prime else "Bukan bilangan prima")
