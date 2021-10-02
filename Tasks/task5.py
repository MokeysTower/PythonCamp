#phone number

#creat the massive of numbers there is can be only 9 numbers 0-9
def addmembers(q):
    z = []
    for i in range(len(q)):
        z.append(q[i])
    return z

x = input('Write 9 numbers (0-9) for create phone number\n')
if len(x) == 9:
    q = addmembers(x)
    print(f'+7({q[0]}{q[1]}{q[2]}) {q[3]}{q[4]}{q[5]}-{q[6]}{q[7]}{q[8]}')
else:
    print('You writed uncorrect number of numbers\n\n')