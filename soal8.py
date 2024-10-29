jumlah = 0
for i in range(2,11,2):
    if i < 10 :
        print (i,end=" + ")
    else :
        print (i,end=" = ")
    jumlah = jumlah + i
print (jumlah)