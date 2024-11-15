hargaBarang = []
for i in range(4):
    harga = float(input(f"masukan harga barang ke {i+1} :Rp."))
    hargaBarang.append(harga)

jumlah = sum(hargaBarang)
if jumlah > 100000 :
    diskon = harga - ((harga * 5 )/ 100)  
    total = jumlah - diskon
    print (f"""
total harga barang yang anda beli adalah Rp.{int(total)}
dengan potongan diskon sebesar Rp.{int(diskon)}
""") 
else :
    print(f"harga barang yang harus anda bayar adalah Rp.{int(jumlah)}")  