import copy
from numpy import array, zeros
#bentuk matriks dari SPL
a = array([[4,-1,-1],[-1,3,-1],[-1,-1,5]], float)
n = len(a)
c = zeros((n,n))
b = zeros((n,n))

print(a)

#perhitungan adjoin
for i in range(0,n):
    for j in range(0,n):
        bs = (i+1)%3
        bd = (i+2)%3
        ks = (j+1)%3
        kd = (j+2)%3
        c[i,j] = a[bs,ks]*a[bd,kd]-a[bs,kd]*a[bd,ks]
        print(c[i,j])
        print("")
    print("batas")
print(c)

#determinan matriks a
su = 0
for i in range(0,n):
    w =(i+1)%3
    v =(i+2)%3
    su += a[0,i]*(a[1,w]*a[2,v]-a[2,w]*a[1,v])
print(f"sum: {su}")

#inverse = adjA/detA
for i in range(0,n):
    for j in range(0,n):
        b[i,j] = c[j,i]
print(b)
invers = b/su
print("invers matriks dengan metode adjoin:")
print(invers)