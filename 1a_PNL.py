import math
L = 0.5
#induktansi dalam satuan henri
C = 10e-6
#kapasitansi dalam satuan farad

#fungsi f terhadap R
def fox(R):
    #persamaan pada soal 
    f = (1/(2*math.pi))*(((1/(L*C))-((R/(2*L))**2))**0.5)
    return f

#turunan fungsi f terhadap R
def f1x(R):
    #turunan pertama persamaan pada soal
    p = (1/(8*math.pi))*(1/(((1/(L*C))-((R/(2*L))**2))**0.5))*(-R/(L**2))
    return p

print(f"contoh nilai dari fungsi f: {fox(20)}")
print(f"contoh nilai dari turunan fungsi f: {f1x(100)}")
