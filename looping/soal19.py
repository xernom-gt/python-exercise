data = int(input("berapa nomor ? :"))
jumlah = []

for i in range(data):
    no = int(input("nilainya berapa? :"))
    jumlah.append(no)
jumlah1 = sum(jumlah) / data
jumlah2 = sum(jumlah)

print (f"""
untuk jumlah nya adalah {jumlah2}
dan untuk rata ratanya adalah {int(jumlah1)}

""")