#for this programm place this program near file (in same folder)
x = input('Write please file name (only name)\n').replace( '.txt', '' )

try:
    with open(f'{x}.txt','r') as h:
        y = h.readlines()
        h.close()
    z = []
    for i in range(len(y)):
        z.append(y[i].replace('\n', ''))
    f=0
    for i in range(len(z)):
       f += len(z[i])
    print(f) 
except Exception as e:
    print('Can\'t found file',e)
