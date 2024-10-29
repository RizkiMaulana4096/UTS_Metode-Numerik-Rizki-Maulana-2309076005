import math as m
def fox(T):
    f = 5000*m.exp((3500/T)-(3500/298))
    return f

To = 298
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

print(fox(To))
print(f_1f(To)) #selisih maju
print(f_1b(To)) #selisih mundur
print(f_1avg(To)) #selisih tengah
print(dif_fox(To)) #emtode eksak
