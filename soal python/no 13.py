x = float(input('"masukan nilai x :'))
y = float(input('"masukan nilai y :'))
z = float(input('"masukan nilai z :'))

number = [x, y, z]

largest = max(number)
smallest = min(number)
number.remove(largest)
number.remove(smallest)
middle = number[0]

print("="*30)
print("Nilai terbesar:", largest)
print("Nilai menengah:", middle)
print("Nilai terkecil:", smallest)
print("="*30)