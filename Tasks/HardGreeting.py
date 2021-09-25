name = input('Write yuor name ')
if name=='Ann':
    print('Hello, '.lower(), name,'! Did you want to see new products?'.lower())
elif name=='Abby' or name=='Garry':
    secondname = input('Name of togeherwyaer ')
    if secondname=='Abby' or secondname=='Garry':
        print('Hello, Good boys! Did you want to see new products?')
    else:
        print(f'Hello, {name}! Did you want to see new products?')
elif name=='Braver':
    print('Hello, '.upper(), name,'! Did you want to see new products?'.upper())
elif name=='HeadChop':
    print(f'Hello, {name}! Did you want to see new products?')
else:
    print('Hello! Can I help you?')


