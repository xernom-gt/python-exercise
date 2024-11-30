start = int(input("Masukkan angka mulai: "))
end = int(input("Masukkan angka akhir: "))
for num in range(start, end + 1):
    if num % 2 != 0:
        print(num, end=" ")
