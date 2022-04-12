import numpy as np
a = np.array([1,2,3,4,5])
print(type(a))

b = np.array([[1,2,3,4,5], [11,12,13,14,15,]])
print(b)

c = np.array([1,2,3,4,5,6,7,8], ndmin= 2)
print(c)

print(b.shape)

b.shape = (5,2)
print(b)

print(b.ndim, b.shape)

a = np.arange(24)
print(a.ndim, a.shape)
b = a.reshape(2,4,3)
print(b)

a = np.empty(shape=(3,4), dtype=int)
print(a)

# convert sequences to array
l = [1,2,3,4,5,6,7,8]
t = (1,2,3,4,5,6,7,8)
p = {1,2,3,4,5,6,7,8}
n = np.asarray(l)
n1 = np.asarray(t)
n2 = np.asarray(p)
print(type(n), type(n1), type(n2))

l = range(50)
for i in l:
    print(i)
print(l, type(l))

l = range(5)
it = iter(l)
print(type(it), type(l))
na = np.fromiter(l, dtype=int)
na2 = np.asarray(l)
print(na, na2)
na = np.arange(10, 20, 2)
print(na)
n = np.array(range(10))
s = slice(4,8,2)
print(n[4:8:2], n[s])
n = np.arange(10)
print(n, type(n))


# boolean of nd array
n = np.arange(10)
n = n[n>5]
print(n)

# iterating arrays
n = np.arange(0,100, 10)
n = np.reshape(n, (5,2))
print(n)
for i in np.nditer(n):
    print(i)
for i in n:
    print(i)

n = n.reshape(2,5)
print(n)
for i in np.nditer(n, op_flags = ['readwrite']):
    i[...] = i*2

print(n)

n1 = np.arange(0, 20, 2).reshape(5,2)
n2 = np.arange(20, 40, 2).reshape(5,2)
print(n1)
print(n2)
for i, j in np.nditer([n1, n2]):
    print("{}:{}".format(i, j))
    r = i*j
    print("result: ", r)

f = n1.flatten()
print(f)

# arithmetic operations
n = np.arange(9, dtype=float).reshape(3,3)
a = [10, 20, 30]
r = np.multiply(n, a)
print(r)

# mean

n = np.arange(9).reshape(3,3)
m = np.mean(n, axis=0)
m = np.mean(n, axis=1)
print(n, m)

n = np.array([[1, 4], [8, 6]])
n = np.sort(n, axis=0)
print(n)

dt = np.dtype([('name', 'S10'), ('age', int)])
a = np.array([('rava', 21), ('aziz', 89), ('islom', 99)], dtype = dt)
a = np.sort(a, order = 'name')
print(a)

a = np.array([[20, 45, 33], [66, 54, 10], [46, 32, 88]])
am = np.argmax(a, axis=0)
print(am)

n = np.arange(9).reshape(3,3)
print(n)
m = np.where(n>3)
print("My array: ",n[m])


# numpy matplotlib
from matplotlib import pyplot as plt
n = np.arange(1,11)
y = 2*n+5
print(y)
plt.title("Matplotlib demo")
plt.xlabel(n)
plt.ylabel(y)
#plt.plot()
#plt.show()

# making two plot
x = np.arange(0, 3 * np.pi, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.subplot(2,1,1)
plt.plot(x, y1)
plt.title("Sinus")

plt.subplot(2,1,2)
plt.plot(x, y2)
plt.title("Cosine")

#plt.show()
a = np.arange(1,49).reshape(6,8)
print(a)

np.save('rauf_file', a)

# load file from out disk
b = np.load('rauf_file.npy')
d = b*3
print(d)

a = np.arange(1,82).reshape(9,9)
print(a)
np.savetxt('rauf_file_txt', a)
b = np.loadtxt('rauf_file_txt')
print(b*np.pi)

