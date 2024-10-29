import math as m
import matplotlib.pyplot as plt

def fox(T):
    f = 5000*m.exp((3500/T)-(3500/298))
    return f
To = 250 #suhu awal
Ta = 350 #suhu akhir
In = 10 # interval
a = []
b = []
c = []
x = []
for i in range(To, Ta+In,In):
    x.append(i)

h = 1e-6
#selisih maju
def f_1f(T):
    r = (fox(T+h)-fox(T))/h
    return r
#selisih mundur
def f_1b(T):
    r = (fox(T)-fox(T-h))/h
    return r
#selisih tengah
def f_1avg(T):
    avg = (f_1f(T) + f_1b(T))/2
    return avg
#metode eksak
def dif_fox(T):
    g = -(17_500_000/(T**2))*m.exp((3500/T)-(3500/298))
    return g

#perhitungan 
for i in range(To, Ta+In,In):
    print(i)
    print(f"fungsi:{fox(i)}") #selisih maju
    a.append((f_1f(i)-dif_fox(i))/dif_fox(i))
    print(f"selisih maju: {f_1f(i)}") #selisih maju
    b.append((f_1b(i)-dif_fox(i))/dif_fox(i))
    print(f"selisih mundur: {f_1b(i)}") #selisih mundur
    c.append((f_1avg(i)-dif_fox(i))/dif_fox(i))
    print(f"selisih tengah: {f_1avg(i)}") #selisih tengah
    print(f"metode eksak: {dif_fox(i)}") # metode eksak

#grafik error relatif
plt.plot(x,a) #biru
plt.plot(x,b) #oren
plt.plot(x,c) #hijau
plt.show()