from numpy import array, zeros
#persamaan dalam bentuk matriks
a = array([[4,-1,-1],[-1,3,-1],[-1,-1,5]], float)
b = array([5,3,4], float)

n = len(b)
x = zeros(n, float)
#tahap eliminasi
for k in range(0,n):
    for i in range(k + 1, n):
        if a[i,k] == 0.0: 
            continue
        #penyamaaan koefisian
        coef = a[i , k]/a[k, k]
        #eliminasi varibel
        for j in range(k, n):
            a[i, j] = a[i, j] - coef*a[k, j]
        #penyamarataan kedua ruas   
        b[i] = b[i] - b[k]*coef
        
#tahap substitusi
x[n-1] = b[n-1]/a[n-1,n-1]
for i in range(n-2,-1,-1):
    su = 0
    for j in range(i+1, n):
        su += a[i,j] * x[j]
    x[i] = (b[i]-su )/a[i, i]
print("matriks akhir:\n",a)
print("\nsolusi dengan metode gauss naive:")
print('[x. y. z.] =', x)