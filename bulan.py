bulan = ['januari','februari','maret','april','mei','juni','juli','agustus','september','oktober','november','desember',]

bulan[7] = 'august'
bulan[0] = 'january'
bulan.append ('muharram')
for x,y in enumerate(bulan):
    print (f"bulan ke- {x+1} yaitu {y}")