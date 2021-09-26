food = [
    ["Apple", 30], 
    ["Cake", 10], 
    ["Coffee", 100],
    ["Chocolate", 10],
    ["Orange", 50],
    ["Flour", 3],
    ["Mushrooms", 60], 
    ["Beer", 10]
]
spells = [
    ["Froggy", 15], 
    ["Ice", 29], 
    ["Fire", 99],
    ["Thunderbolt", 14],
    ["Cure", 50],
    ["Trap", 17],
    ["Search", 43], 
    ["Bag", 1000]
]
weapons = [
    ["Sword", 100], 
    ["Axe", 29], 
    ["Shield", 80],
    ["Bow", 40],
    ["Mace", 20],
    ["Spear", 10],
    ["Dart", 85], 
    ["Zweinhander", 1]
]

arr = [food,spells,weapons]
while True:
    UserName = input('Welcome,How I can call you?\n').lower() 
    if UserName == 'manager close':
        break
    elif len(UserName.lower().split(' ')) == 5:
        UserName2=UserName.split(' ')
        if UserName2[2] == '1' or UserName2[2][0] == 'f':
            while True:
                print('\n')
                for i in range(len(food)):
                    if UserName2[3].title() == food[i][0]:
                        food[i][1] += abs(int(UserName2[4]))
                        print(f'You add {UserName2[3].title()}, now we have {food[i][1]}')
                        print('\n')
                        break
                if UserName2[3].title() != food[i][0]:
                    food.append([UserName2[3].title,int(UserName2[4])])
                    print(f'\nYou added new product {UserName2[3].title()} how we have {UserName2[4]}\n')
                    
                break
        elif UserName2[2] == '2' or UserName2[2][0] == 's':
            while True:
                print('\n')
                for i in range(len(spells)):
                    if UserName2[3].title() == spells[i][0]:
                        spells[i][1] += abs(int(UserName2[4]))
                        print(f'You add {UserName2[3].title()}, now we have {spells[i][1]}')
                        print('\n')
                        break
                    
                if UserName2[3].title() != spells[i][0]:
                    spells.append([UserName2[3].title,int(UserName2[4])])
                    print(f'\nYou added new product {UserName2[3].title()} how we have {UserName2[4]}\n')
                break
        elif UserName2[2] == '3' or UserName2[2][0] == 'w':
            while True:
                print('\n')
                for i in range(len(weapons)):
                    if UserName2[3].title() == weapons[i][0]:
                        weapons[i][1] += abs(int(UserName2[4]))
                        print(f'You add {UserName2[3].title()}, now we have {weapons[i][1]}')
                        print('\n')
                        break
                    
                if UserName2[3].title() != weapons[i][0]:
                    weapons.append([UserName2[3].title,int(UserName2[4])])
                    print(f'\nYou added new product {UserName2[3].title()} how we have {UserName2[4]}\n')
                break
        continue
    while True:
        print('Categories:\n1.Food\n2.Spells\n3.Weapons\n\nWrite\'out\' for exit')
        choise = input('\nWhich category you chouse?\n').lower()
        if choise == 'out':
            print(f'\nGoodbye,{UserName.title()}\n\n')
            break
        elif choise[0] == '1' or choise[0] == 'f':
            while True:
                print('\n')
                for i in range(len(food)):
                    print(f'{food[i][0]} - {food[i][1]}')
                choise2 = input('\nChoose product\n').lower()
                for i in range(len(food)):
                    
                    if choise2.title() == food[i][0]:
                        howmuch = int(input((f'How much you want {choise2.title()}?\n')))
                        if howmuch > food[i][1]:
                            print('I\'m sorry, we haven\'t this amout of this products.'.upper())
                            continue
                        food[i][1] -= howmuch
                        print(f'Thank you,{UserName.title()}! Something more?') 
                        if food[i][1] <= 0:
                            food.pop(i)
                            print(f'You took last {choise2.title()}')
                        print('\n')
                        break
                if choise2.title() != food[i][0]:
                    print('\nThis porduct ended or isn\'t selling\n'.upper())
                break
        elif choise[0] == '2' or choise[0] == 's':
            while True:
                print('\n')
                for i in range(len(spells)):
                    print(f'{spells[i][0]} - {spells[i][1]}')
                choise2 = input('\nChoose product\n').lower()
                for i in range(len(spells)):
                    if choise2.title() == spells[i][0]:
                        while True:
                            howmuch = int(input((f'How much you want {choise2.title()}?\n')))
                            if howmuch > spells[i][1]:
                                print('I\'m sorry, we haven\'t this amout of this products.')
                                continue
                            spells[i][1] -= howmuch
                            print(f'Thank you,{UserName.title()}! Something more?') 
                            if spells[i][1] <= 0:
                                spells.pop(i)
                                print(f'You took last {choise2.title()}')
                            break
                        print('\n')
                        break
                if choise2.title() != spells[i][0]:
                    print('\nThis porduct ended or isn\'t selling\n'.upper())
                break
        elif choise[0] == '3' or choise[0] == 'w':
            while True:
                print('\n')
                for i in range(len(weapons)):
                    print(f'{weapons[i][0]} - {weapons[i][1]}')
                choise2 = input('\nChoose product\n').lower()
                for i in range(len(weapons)):
                    if choise2.title() == weapons[i][0]:
                        while True:
                            howmuch = int(input((f'How much you want {choise2.title()}?\n')))
                            if howmuch > weapons[i][1]:
                                print('I\'m sorry, we haven\'t this amout of this products.'.upper())
                                continue
                            weapons[i][1] -= howmuch
                            print(f'Thank you,{UserName.title()}! Something more?') 
                            if weapons[i][1] <= 0:
                                weapons.pop(i)
                                print(f'You took last {choise2.title()}')
                            break
                        print('\n')
                        break
                if choise2.title() != weapons[i][0]:
                    print('\nThis porduct ended or isn\'t selling\n'.upper())
                break


