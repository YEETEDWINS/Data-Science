import numpy as np

a = [2, 3, 6, "s", True, 289, False]
print(type(a))
b = np.array([2, 7, 3992, 29349, 20, 9291])
print(type(b))

c = np.zeros(10)
print(c)

d = np.ones(10)
print(d)

e = np.array([[2 , 3912, 39], [49, 4903, 201], [3, 67, 3932], [3, 53, 21]])
print(e)
print("")
print(e.ndim)
print(e.nbytes)
print(e.shape)
print(e.size)
print("")

f = np.arange(1, 100, 3)
print(f)

print(np.random.randint(1, 50))

g = np.random.rand(3, 5)
print(g)
print(g.shape)

h = np.arange(15, 45).reshape(6, 5)
print(h)

i = np.array([4, 18902, 28934,34783, 5895, 9430989,689834954095878493,7887966])
sortedI = np.sort(i)
print(sortedI)

j = np.array([34, 4, 29, 32, 2])
print(j[:4])
print(j[1:4])
print(j[4:0:-1])