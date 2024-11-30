gaji_awal = 3000000

jam_kerja = int(input("Masukkan jumlah jam kerja: "))

menit_tambahan = int(input("Masukkan jumlah menit tambahan: "))

upah_per_jam = 500000
upah_per_menit = 1000

total_upah = gaji_awal + (jam_kerja * upah_per_jam) + (menit_tambahan * upah_per_menit)

print("\n=== Perhitungan Gaji ===")
print(f"Gaji awal: Rp{gaji_awal:,}")
print(f"Tambahan dari {jam_kerja} jam kerja: Rp{jam_kerja * upah_per_jam:,}")
print(f"Tambahan dari {menit_tambahan} menit kerja: Rp{menit_tambahan * upah_per_menit:,}")
print(f"Total gaji: Rp{total_upah:,}")
