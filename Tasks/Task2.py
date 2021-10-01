def addmembers(q):
    z=[]
    for i in range(len(q)):
        if i != 0 and i%3 == 0 or i != 0 and i%5 == 0:
            z.append(i)
    f = 0
    for i in range(len(z)):
        f += z[i]
    return(f)

def calculation(z):
    if len(z) == 1 and z != '0':
        return int(z) 
    q = str(addmembers(z))
    return calculation(q)
z = str(abs(int(input('Write the number\n'))))
print(calculation(z))

#This program doesn't work