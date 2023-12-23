waktu_awal = input("\nMasukkan waktu awal (HH:MM): : ")
jam_awal, menit_awal = map(int, waktu_awal.split(":"))

jam_pengurangan = int(input("Masukkan jumlah jam pengurangan: "))
menit_pengurangan = int(input("Masukkan jumlah menit pengurangan: "))

jam_hasil = jam_awal - jam_pengurangan
menit_hasil = menit_awal - menit_pengurangan

if menit_hasil < 60:
    jam_hasil -= 1
    menit_hasil += 60

if jam_hasil >= 24:
    jam_hasil -= 24

print(f"Waktu sekarang menunjukkan Pukul {jam_hasil:02d}:{menit_hasil:02d}")