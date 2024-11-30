n = int(input("Masukkan jumlah elemen dalam list: "))
my_list = [int(input(f"Masukkan elemen ke-{i+1}: ")) for i in range(n)]
print("List yang dimasukkan:", my_list)
