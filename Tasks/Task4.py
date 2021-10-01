def reverse3(z):
    z = str(z)
    q = []
    z1 = ''
    for i in range(len(z)):
        q.append(z[i])
    q.sort()
    q.reverse()
    for i in range(len(q)):
        z1 += q[i]
    z2 = int(z1)
    return z2


x = input('Write number\n')
print(reverse3(x))