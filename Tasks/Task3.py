def reverse2(z):
    q = []
    z1 = ''
    for i in range(len(z)):
        q.append(z[i])
    q.reverse()
    for i in range(len(q)):
        z1 += q[i]
    return z1

x = input('Write words\n').split(' ')
if len(x) == 1:
    if len(x[0]) > 4:
        print(reverse2(x[0]))
    else:
        print(x)
elif len(x) > 1:
    z = ''
    for i in range(len(x)):
        if len(x[i]) <= 4:
            z += f' {x[i]}'
        else:
            y = reverse2(x[i])
            z += f' {y}'
    print(z)
