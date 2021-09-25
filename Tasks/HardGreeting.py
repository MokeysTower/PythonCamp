while True:
    name = input('Write yuor name ')
    gre = 'Hello, 1! Did you want to see new products?'
    if name=='Ann':
        gre = gre.lower() 
        print(gre.replace('1', name))
    elif name=='Abby' or name=='Garry':
        secondname = input('Name of togeherwyaer ')
        if secondname=='Abby' or secondname=='Garry':
            print(gre.replace('1', 'Good Boys'))
        else:
            print(gre.replace('1', name))
    elif name=='Braver':
        gre = gre.upper() 
        print(gre.replace('1', name))
    elif name=='HeadChop' or name=='Headchop':
        print(f'Hello, {name}! Did you want to see new products?')
    elif name=='out':
        break
    else:
        print('Hello! Can I help you?')


