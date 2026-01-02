i = [1, 2, 3, 4, 5]
j = i
j[0] = 100
print("j =", j)
print("i =", i)

i = [1, 2, 3, 4, 5]
j = i.copy()
j[0] = 100
print("j =", j)
print("i =", i)

x = 20
y = x
y = 5
print(id(x))
print(id(y))
print("x =", x)
print("y =", y)

x = [20, 30, 40]
y = x.copy()
y[0] = 5
print(id(x))
print(id(y))
print("x =", x)
print("y =", y)