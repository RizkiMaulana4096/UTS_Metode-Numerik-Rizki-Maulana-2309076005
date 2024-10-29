from numpy import array, zeros
import copy
#bentuk matriks dari SPL
a = array([[4,-1,-1],[-1,3,-1],[-1,-1,5]], float)
#matriks a
b = array([5,3,4], float)
#hasil setiap persamaan

n = len(b)
#da akan menjadi determinan matriks a
dA = 0
#determinan matriks a
for i in range(0,n):
    w =(i+1)%3
    print(w)
    v =(i+2)%3
    print(v)
    dA += a[0,i]*(a[1,w]*a[2,v]-a[2,w]*a[1,v])
    print(dA)
print(f"sum:{dA}")

sol = zeros(n, float)
r = zeros(n, float)
c = zeros((n,n))

print(a)

for i in range(0,n):
    c = zeros((3,3))
    c = copy.deepcopy(a)
    for j in range(0,n):
        c[j,i] = b[j]
    detsub = 0
    for k in range(0,n):
        w =(k+1)%3
        print(w)
        v =(k+2)%3
        print(v)
        detsub += (c[0,k]*(c[1,w]*c[2,v]-c[2,w]*c[1,v]))
        r[i] = detsub
    print(f"det [{i}]:{detsub}")
    print(c)
    print(" ")
print(a)

for i in range(0, n):
    sol[i] = r[i]/dA

print(f"solusi [x. y. z.] = {sol}")