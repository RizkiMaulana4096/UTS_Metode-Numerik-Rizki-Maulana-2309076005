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

n = 0
s = 0.1
while abs(f_1(x)) > s and n < 1000:
    n += 1 #counting banyak iterasi
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
print(f"n_iterasi = {n}")
print(f"nilai R = {x}") #hasil newton raphson adalah bagian realnya
print(f"error = {f_1(x)}")
