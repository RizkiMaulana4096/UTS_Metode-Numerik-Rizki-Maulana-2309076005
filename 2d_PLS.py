from numpy import array
#bentuk matriks dari SPL
a = array([[4,-1,-1],[-1,3,-1],[-1,-1,5]], float)
b = array([5,3,4], float)

n = len(b)
#eliminasi ke 1
for k in range(0,n):
    for i in range(k + 1, n):
        if a[i,k] == 0.0: 
            continue
        coef = a[i , k]/a[k, k]
        for j in range(k, n):
            a[i, j] = a[i, j] - coef*a[k, j]
        b[i] = b[i] - b[k]*coef
#eliminasi ke 2
for k in range(n-1,-1,-1):
    for i in range(0, k):
        coef = a[i,k]/a[k,k]
        a[i,k] = 0
        b[i] = b[i] - b[k]*coef
#solusi dengan metode gauss-jordan
for i in range(0,n):
    for j in range(0,n):
        if i==j:
            b[i] = b[i]/a[i,j] 
            a[i,j]= 1
print("matriks akhir:\n",a)
print("\nsolusi dengan metode gauss jordan:")
print("[x. y. z.] =",b)