waktu_awal = input("\nMasukkan waktu awal (HH:MM): : ")
jam_awal, menit_awal = map(int, waktu_awal.split(":"))

jam_tambahan = int(input("Masukkan jumlah jam tambahan: "))
menit_tambahan = int(input("Masukkan jumlah menit tambahan: "))

jam_hasil = jam_awal + jam_tambahan
menit_hasil = menit_awal + menit_tambahan

if menit_hasil >= 60:
    jam_hasil += 1
    menit_hasil -= 60

if jam_hasil >= 24:
    jam_hasil -= 24

print(f"Waktu sekarang menunjukkan Pukul {jam_hasil:02d}:{menit_hasil:02d}")