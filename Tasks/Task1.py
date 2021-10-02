def addmembers(q):
    z=[]
    f = 0
    for i in range(q):
        if i != 0 and i%3 == 0 or i != 0 and i%5 == 0:
            z.append(i)
    for i in range(len(z)):
        f += z[i]
    return(f)


