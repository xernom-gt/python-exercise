jumlah = 0
for i in range (5):
    if i < 4 :
        print (i+1,end="+")
    else :
        print (i+1,end="=")
    jumlah = jumlah + (i+1)
print (jumlah)