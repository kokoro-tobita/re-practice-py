n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n.append(100)
print(n)
n.insert(0, 100)
print(n)
n.pop()
print(n)
n.pop(0)
print(n)

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
a.extend(b)

r = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
r.sort()
print(r)
r.sort(reverse=True)
print(r)

s = "My name is Mike."
to_split = s.split(" ")
print(to_split)
x = " ".join(to_split)
print(x)