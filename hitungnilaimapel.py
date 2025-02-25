# 2. Menghitung nilai rata-rata seorang siswa dari 5 mata pelajaran ( IPA, IPS, MTK, ENGLISH, INDONESIA)
Mapel_IPA = int(input("Masukan nilai ipa :"))
Mapel_IPS = int(input("Masukan nilai ips :"))
Mapel_MTK = int(input("Masukan nilai mtk :"))
Mapel_English = int(input("Masukan nilai english :"))
Mapel_Indonesia = int(input("Masukan nilai indonesia :"))

ratarata_seluruh_mapel = (Mapel_IPA + Mapel_IPS + Mapel_MTK + Mapel_English + Mapel_Indonesia)/5
nilai = [Mapel_IPA, Mapel_IPS, Mapel_MTK, Mapel_English, Mapel_Indonesia]
print("Hitung rata-rata nilai seluruh mata pelajaran,",ratarata_seluruh_mapel)

# 3. mengecek nilai lulus atau tidak lulus dengan kriteria
# - Dinyatakan lulus, jika rata-rata nilai keseluruhan dari mata pelajaran lebih dari 75
# - Dinyatakan lulus, jika hanya 2 mata pelajaran yang dibawah 50
# - Mendapatkan nilai sempurna (100) dari salah satu mata pelajaran 

nilai_dibawah_50 = 2
if(Mapel_IPA < 50):
    nilai_dibawah_50 += 1
if(Mapel_IPS < 50):
    nilai_dibawah_50 += 1 
if(Mapel_MTK < 50):
    nilai_dibawah_50 += 1 
if(Mapel_English < 50):
    nilai_dibawah_50 += 1 
if(Mapel_IPA < 50):
    nilai_dibawah_50 += 1 

if (ratarata_seluruh_mapel >= 75):
    print ("lulus, karena rata-rata lebih dari 75")
elif (nilai.count(100) >= 1):
    print("lulus, karena mendapatkan nilai sempurna dari salah satu mata pelajaran")
elif (nilai_dibawah_50 == 2):
    print("lulus, karena hanya 2 nilai mata pelajaran yang dibawah 50 ")
else :
    print("tidak lulus")

    
        