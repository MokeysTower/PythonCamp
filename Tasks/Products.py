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
    while True:
        print('Categories:\n1.Food\n2.Spells\n3.Weapons')
        choise = input('\nWhich category you chouse?\n').lower()
        if choise[0] == '1' or choise[0] == 'f':
            while True:
                print('\n')
                for i in range(len(food)):
                    print(f'{food[i][0]} - {food[i][1]}')
                choise2 = input('\nChoose product\n').lower()
                for i in range(len(food)):
                    if choise2.title() == food[i][0]:
                        while True:
                            howmuch = int(input((f'How much you want {choise2.title()}?\n')))
                            if howmuch > food[i][1]:
                                print('I\'m sorry, we haven\'t this amout of this products.')
                                continue
                            food[i][1] -= howmuch 
                            if food[i][1] <= 0:
                                food.pop(i)
                                print(f'You took last {choise2.title()}')
                            break
                        print('\n')
                        break
                    break
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
                            if spells[i][1] <= 0:
                                spells.pop(i)
                                print(f'You took last {choise2.title()}')
                            break
                        print('\n')
                        break
                    break
                break
#Так тут не добавлен вариант когда человек ввел не то название (сразу выкидывает в категории)
#Тут нет треьей категории и доступа для менеджера )))