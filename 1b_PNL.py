import math
L = 0.5
#induktansi dalam satuan henri
C = 10e-6
#kapasitansi dalam satuan farad
a = 0
b = 100
u = 0
n = 100
e = 0.1

#fungsi f terhadap R
def fox(R):
    f = (1/(2*math.pi))*(((1/(L*C))-((R/(2*L))**2))**0.5)-70
    return f
    #dikurang 70 agar dengan metode biseksi dapat dicari nilai fungsi yang akan menghasilkan frekuensi resonansi sebesar 70 Hz
    #apabila digunakan frekuensi 1000 Hz maka tidak ditemukan solusi, berdasarkan grafik nilai maksimum dari fungsi ini berkisar 71.176254...
def avg(a,b):
    x = (a + b)/2
    return x
r = b - a
while r > e and u < n:
    p = avg(a,b)
    l = fox(p)*fox(a) 
    #pengecekan persamaan tanda pada fungsi dengan input "rata-rata" dan fungsi dengan input a
    if l < 0:
        b = p
        print(b)
    else:
        a = p
        print(a)
    r = b - a
    #nilai error
    print(f"nilai r = {r}")
    u += 1 #counting banyak iterasi
#mengambil nilai tengah dari nilai a dan b akhir supaya mendapatkan hasil biseksi
t = avg(a,b)

print(f"nilai hasil biseksi: {t}")
print(f"jumlah perulangan: {u}")
#selisih nilai hasil fungsi dengan 70 Hz
print(f"f(x): {fox(t)}")