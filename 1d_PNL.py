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

c =[]
d =[]

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
        c.append(b)
    else:
        a = p
        print(a)
        c.append(a)
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


import math
L = 0.5

#induktansi dalam satuan henri
C = 10e-6
f = 70
#bila frekuensi 1000 Hz dicari nilai R nya yang tepat maka solusi tidak bisa didapatkan
#frekuensi yang digunakan 70 Hz karena mendekati nilai maksimum dari fungsi ini
#kapasitansi dalam satuan farad

def f_1(R):
    g = (1/(2*math.pi))*(((1/(L*C))-((R/(2*L))**2))**0.5)-70
    return g

def f_2(R):
    p = (1/(2*math.pi))*(((1/(L*C))-((R/(2*L))**2))**-0.5)*(-2*R/((2*L)**2)) #turunan pertama fungsi dalam akar
    return p

x = 500 #nilai awal

k = 0
s = 0.1
while abs(f_1(x)) > s and k < 1000:
    k += 1 #counting banyak iterasi
    if f_2(x) != 0:
        if f_1(x) != 0:
            print(x)
            x -= f_1(x)/f_2(x)
            print(f_1(x)/f_2(x))
            print(x)
            print(" ")
        else:
            print("nilai divergen")
            break
    else:
        print("Error dibagi nol")
        print(x)
        break

    #(1/(L*C))-((R/(2*L))**2)-((4*(math.pi)*f)**2)
print(f"n_iterasi = {k}")
print(f"nilai R = {x}") #hasil newton raphson adalah bagian realnya
print(f"error = {f_1(x)}")