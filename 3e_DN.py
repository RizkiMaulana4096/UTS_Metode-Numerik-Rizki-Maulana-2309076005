import math as m
def fox(T):
    f = 5000*m.exp((3500/T)-(3500/298))
    return f

To = 298
h = 1e-6
#selisih maju
def f_1f(T,h):
    r = (fox(T+h)-fox(T))/h
    return r
#selisih mundur
def f_1b(T,h):
    r = (fox(T)-fox(T-h))/h
    return r
#selisih tengah
def f_1avg(T,h):
    avg = (f_1f(T,h) + f_1b(T,h))/2
    return avg
def ext_Ric(T,h):
    x = f_1avg(T,h) + (1/3)*(f_1avg(T,h)-f_1avg(T,2*h))
    return x
#metode eksak
def dif_fox(T):
    g = -(17_500_000/(T**2))*m.exp((3500/T)-(3500/298))
    return g

print(f"hasil Ekstrapolasi Richardson: {ext_Ric(To,h)}")
print("")
print(f"nilai f(x): {fox(To)}")
print(f"hasil metode selisih maju: {f_1f(To,h)}")
print(f"hasil metode selisih mundur: {f_1b(To,h)}")
print(f"hasil metode selisih tengah: {f_1avg(To,h)}")
print(f"hasil metode eksak: {dif_fox(To)}")