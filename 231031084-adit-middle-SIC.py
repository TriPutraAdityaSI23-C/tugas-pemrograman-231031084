''' UTS
1. Buat variabel jenis list berikut.
    
    Bio =  ['Institut Teknologi Bacharuddin Jusuf Habibie',
            'Parepare',
            'Jurusan Sains',
            'Nama Lengkap',
            'NIM',
            'Tanggal-Bulan-Tahun Lahir',
            'S1',
            'Sistem Informasi C',
            'aktif',
            'ganjil',
            '2023-2024',
            'kartu hasil studi mahasiswa']
#(NOTED: sesuaikan dengan data anda)

2. Buat variabel nested list berikut.

MK =   [['Matkul1','Matkul2','Matkul3','Matkul4','Matkul5','Matkul6','Matkul7','Matkul8'],
        [3,2,3,2,3,3,3,2],
        ['22A1209','22A1210','22A1211','22A1212','22A1213','22A1214','22A1215','22A1216'],
        [3.50,3.00,3.75,4.00,3.75,3.50,3.75,3.00]]

#(NOTED: Ubah Nama Matakuliah, Jumlah SKS, dan Nilai)

3. Buat Kode dengan hasil runing seperti berikut.


            INSTITUT TEKNOLOGI BACHARUDDIN JUSUF HABIBIE
                           JURUSAN SAINS
                    KARTU HASIL STUDI MAHASISWA
                          GANJIL 2023/2024

                    
Nama Lengkap    : NAMA LENGKAP
NIM             : NIM
Program/Prodi   : S1/Sistem Informasi C
Tahun Masuk     : 2023-Ganjil
Status          : Aktif
|--|--   12   --|--             31            --|-- 7 --|--    13   --|
-----------------------------------------------------------------------
No. Kode        |           Mata Kuliah         |  SKS  | Nilai (0-4) |
-----------------------------------------------------------------------
1   22A1209     | Matkul1                       |   3   |         3.50|
2   22A1210     | Matkul2                       |   2   |         3.00|
3   22A1211     | Matkul3                       |   3   |         3.75|
4   22A1212     | Matkul4                       |   2   |         4.00|
5   22A1213     | Matkul5                       |   3   |         3.75|
6   22A1214     | Matkul6                       |   3   |         3.50|
7   22A1215     | Matkul7                       |   3   |         3.75|
8   22A1216     | Matkul8                       |   2   |         3.00|
-----------------------------------------------------------------------
                                       TOTAL SKS:   21
-----------------------------------------------------------------------
|---------------------------------71-----------------------------------|
Summary:
Jumlah Mata Kuliah : 8 Mata Kuliah
Nilai Tertinggi    : 4.00  (22A1212 - Matkul4)
Nilai Terendah     : 3.00  (22A1211 - Matkul2)
IP Kumulatif       : 3.00
                                   
                                               Parepare, 25 Oktober 2023



                                                     NAMA LENGKAP      
                                                     ------------
'''


# Tulis Kode Jawaban di bawah!

bio = ['Institut Teknologi Bacharuddin Jusuf Habibie',
            'Parepare',
            'Jurusan Sains',
            'Tri Putra Aditya',
            '231031084',
            '22-12-2004',
            'S1',
            'Sistem Informasi C',
            'aktif',
            'ganjil',
            '2023-2024',
            'kartu hasil studi mahasiswa']

MK =   [['Kalkulus Dasar','Pengantar Pemograman','Saint Terpadu','Cinta dan Imtaq','Agama Islam','Bahasa','Pendidikan Pancasila','Pengantar Teknologi Informasi'],
        [3,3,3,2,3,2,2,3],
        ['22A1209','22A1210','22A1211','22A1212','22A1213','22A1214','22A1215','22A1216'],
        [3.50,3.00,3.75,4.00,3.75,3.50,3.75,3.00]]

tp =  72
print(f"\n{bio[0].upper().center(tp)}")
print(f"{bio[2].upper().center(tp)}")
print(f"{bio[-1].upper().center(tp)}")
print(f"{bio[-3].upper().center(tp)}")
print(f"{bio[-2].center(tp)}")
print(f"\nNama Lengkap\t: {bio[3].upper()}")
print(f"NIM\t\t: {bio[4]}")
print(f"Program/studi\t: {bio[6]}/{bio[7]}")
print(f"Tahun Masuk\t: {bio[-2][:4]}-{bio[-3]}")
print("|--|--   12   --|--             31            --|-- 7 --|--    13   --|")
print("-"*tp)
print("No. Kode\t|\t\tMata Kuliah\t|  SKS  | Nilai (0-4) |")
print("-"*tp)
print(f"1   {MK[-2][0]}\t| {MK[0][0]}\t\t|   {MK[1][0]}   |\t  {MK[-1][0]}0|")
print(f"2   {MK[-2][1]}\t| {MK[0][1]}\t\t|   {MK[1][1]}   |\t  {MK[-1][1]}0|")
print(f"3   {MK[-2][2]}\t| {MK[0][2]}\t\t\t|   {MK[1][2]}   |\t  {MK[-1][2]}|")
print(f"4   {MK[-2][3]}\t| {MK[0][3]}\t\t|   {MK[1][3]}   |\t  {MK[-1][3]}0|")
print(f"5   {MK[-2][4]}\t| {MK[0][4]}\t\t\t|   {MK[1][4]}   |\t  {MK[-1][4]}|")
print(f"6   {MK[-2][5]}\t| {MK[0][5]}\t\t\t|   {MK[1][5]}   |\t  {MK[-1][5]}0|")
print(f"7   {MK[-2][6]}\t| {MK[0][6]}\t\t|   {MK[1][6]}   |\t  {MK[-1][6]}|")
print(f"8   {MK[-2][7]}\t| {MK[0][7]}\t|   {MK[1][7]}   |\t  {MK[-1][7]}0|")
print("-"*tp)
print(f"\t\t\t\t       TOTAL SKS:   {sum(MK[1])}")
print("-"*tp)
pt = 70
a = "71"
print(f"|{a.center(pt,'-')}|")
print("Summary:")
print(f"Jumlah Mata Kuliah\t: {len(MK[0])} Mata Kuliah")
print(f"Nilai Tertinggi\t\t: {max(MK[-1])}0 ({MK[-2][3]} - {MK[0][3]})")
print(f"Nilai Terendah\t\t: {min(MK[-1])}0 ({MK[-2][-1]} - {MK[0][-1]})")
print("IP Kumulatif\t\t: 3.00")
print(f"{bio[1].rjust(tp)} {bio[5].rjust(tp)}")
print(f"\n\n\n{bio[3].rjust(tp)}")
#print('-'*10.rjust(tp))