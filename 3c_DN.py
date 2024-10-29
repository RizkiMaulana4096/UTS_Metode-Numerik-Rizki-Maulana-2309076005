import math as m
def fox(T):
    f = 5000*m.exp((3500/T)-(3500/298))
    return f

To = 250 #suhu awal
Ta = 350 #suhu akhir
In = 10 # interval

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

for i in range(To, Ta+In,In):
    print(i)
    print(f"fungsi:{fox(i)}") #nilai fungsi
    print(f"selisih maju: {f_1f(i)}") #selisih maju
    print(f"selisih mundur: {f_1b(i)}") #selisih mundur
    print(f"selisih tengah: {f_1avg(i)}") #selisih tengah
    print(f"metode eksak: {dif_fox(i)}") # metode eksak