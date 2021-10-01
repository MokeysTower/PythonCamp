def addmembers(q):
    z=[]
    for i in range(q):
        if i != 0 and i%3 == 0 or i != 0 and i%5 == 0:
            z.append(i)
    return z

def calculation(z):
    q = 0
    for i in range(len(z)):
        q += z[i]
    return(q)

t = int(input('Write the number\n'))
print(calculation(addmembers(t)))