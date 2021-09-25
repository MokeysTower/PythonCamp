arr = [
    ['Alice', True, 100],
    ['Joe', 30, False],
    [True, 'Megan', 200],
    [50, 'Oliver', False],
    [200, True, 'Rassel'],
    ['Molly', True, 2147000000]
]
while True:
    inTekst=input('Write who will take damage and how much\n').lower()
    if (inTekst == 'out'):
        break
    elif (inTekst =='show'):
        for i in arr:
            print(i)
    else:
        x = inTekst.split(' ')
        damage = int(x[1])
        name = x[0].title()
        hero = 'i'
        for y in range(len(arr)):
            z=arr[y]
            for q in range(len(z)):
                if (type(z[q]) == str):
                    break
            if (z[q] == name):
                hero= z[q]
                break
        if (z[q] != name):
                print('I can\'t found this person')
        for q in range(len(z)):
            if (type(z[q]) == bool):
                    break
        if (z[q] == True):
            for q in range(len(z)):
                if (type(z[q]) == int):
                    break
            z[q]-= damage 
            if z[q] <= 0:
                print(f'{hero} died!')
                arr.pop(y)
        else:
            print('Don\'t try little shit')