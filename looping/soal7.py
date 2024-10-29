jumlah = 0 
for i in range(1,6,2):
    if i < 5 :
        print (i,end=" + ")
    else :
        print (i,end=" = ")
    jumlah = jumlah + (i)
print(jumlah)