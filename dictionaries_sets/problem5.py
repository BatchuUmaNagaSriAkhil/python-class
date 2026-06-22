s = {i*i for i in range(1,11)}
m = set(range(2,21,2))

print(s)
print(m)
print(s|m)
print(s&m)
print(s-m)
print(m-s)
print(s^m)