from numpy import array, zeros
#bentuk matriks dari SPL
a = array([[4,-1,-1],[-1,3,-1],[-1,-1,5]], float) #matriks a
print(f"matriks:\n {a}")
b = array([5,3,4], float)
c = zeros((3,3))
n = len(b)
sum = 0
#determinan matriks a
for i in range(0,n):
    w =(i+1)%3
    v =(i+2)%3
    sum += a[0,i]*(a[1,w]*a[2,v]-a[2,w]*a[1,v])
print(f"determinan matriks a: {sum}")

