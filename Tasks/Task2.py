def addmembers(q):
    z=[]
    for i in range(len(q)):
        z.append(q[i])
    f = 0
    for i in range(len(z)):
        f += int(z[i])
    return(f)

def calculation(z):
    if len(z) == 1:
        return int(z) 
    q = str(addmembers(z))
    return calculation(q)

z = str(abs(int(input('Write the number\n'))))
print(calculation(z))