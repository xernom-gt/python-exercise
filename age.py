# bisa berapa banyak orang yang d input
# berapa usianya
# cari rata rata 
# cari usia tertua pertama dan kedua
# cari usia termuda pertama dan kedua
# cari data masing masing untuk usia




def aplication():
    print ("~welcome to brooklyn~")
    jumlah = int(input("how many people ?"))
    data = []
    for x in range (jumlah):
        usia = int(input("how old that people? :"))
        data.append(usia)
    jumlah2 = sum(data) / jumlah
    data.sort()
    umur_tertua = data[0]
    umur_tertua2 = data[1] if jumlah > 1 else None
    umur_termuda = data[-1]
    umur_termuda2 = data[-2] if jumlah > 1 else None
    print (f'average age in this village is {int(jumlah2)} year old')
    print (f'the youngest people is {umur_tertua} year old')
    print (f'the second youngest people is {umur_tertua2} year old')
    print (f'the oldest people is {umur_termuda} year old')
    print (f'the second oldest people is {umur_termuda2} year old')
  

aplication()