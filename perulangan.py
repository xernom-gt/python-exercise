#1.
for x in range (1 , 5) :
    for y in range (5) :
        print (y+1, end=" ")
    print()

#2.
angka = ['A', 'B' , 'C' , 'D']
for i in range (4):
    print (angka[i],'.LU CERDAS')

#3.
jumlah = 0 
for data in range (5):
    print (data+1,'+', end= ' ')
    jumlah = jumlah + (data + 1 )
    
print ('=',jumlah)