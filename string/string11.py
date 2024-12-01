from datetime import datetime

def cetak_hari_tanggal():
    sekarang = datetime.now()

    hari = sekarang.strftime("%A")  
    tanggal = sekarang.strftime("%d")  
    bulan = sekarang.strftime("%B")  
    tahun = sekarang.strftime("%Y")  
    
    print("=== Informasi Tanggal Sekarang ===")
    print(f"Hari   : {hari}")
    print(f"Tanggal: {tanggal}")
    print(f"Bulan  : {bulan}")
    print(f"Tahun  : {tahun}")

cetak_hari_tanggal()
