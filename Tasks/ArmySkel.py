hero = { 
    'health': 100,
    'damage': 10
}
Army = []
id = 0

def addSkeleton():
    global Army
    global id
    x = input('Name of unit \n')
    id += 1
    army1 ={'Name': x,'ID': id,'health':20,'damage':10}
    Army.append(army1)
    print('Unit added\n')
    return

def deletiSkel(z):
    global Army
    for i in range(len(Army)):
        if len(Army[i]) == 1:
            continue
        if Army[i] == z:
            skelt: dict = Army[i] 
            skelt.clear()
    return
    
def alfind(id, Army):
    for skel in Army:
        if skel['ID'] == id:
            return skel
    return 0

def fight(x):
    global Army
    global hero
    z=0
    if len(Army[x-1]) == 1:
        print('Skeleton with this ID dead or not exists\n')
        return
    #raunds
    while True:
        z +=1
        print('\n\nРаунд', z)
        #Hero attacks
        Army[x-1]['health'] = Army[x-1]['health'] - hero['damage']
        if Army[x-1]['health'] == 0:
            skelt: dict = Army[x-1] 
            skelt.clear()
            currHealth = hero['health']
            print(f'\n\nSkeleton can attak, he die after\nHero:\nHealth:{currHealth}\n')
            return
        elif Army[x-1]['health'] != 0:
            hero['health'] -= Army[x-1]['damage']
            if hero['health'] == 0:
                currHealth = Army[x-1]['health']
                print(f'\n\nHero dead.\n\nSkeleton:\nHealth:{currHealth}\n')
                return
            currHealth = hero['health']
            currHealth2 = Army[x-1]['health']
            print(f'Hero:{ currHealth }\nSkeleton:{ currHealth2 }')
        return

while True:
    print('\n\n For create new unit write: \'add unit\'')
    v = input('What we wiil do?').lower()

    #add unit
    if v.split(' ')[0] == 'add':
        addSkeleton()
        continue
    #find
    elif v.split(' ')[0] == 'find':
        x = int(v.split(' ')[1])
        alfind(x, Army)
        print()
    elif v.split(' ')[0] == 'fight':
        x = int(v.split(' ')[1])
        fight(x)
    elif v.split(' ')[0] == 'del':
        x = int(v.split(' ')[1])
        deletiSkel(x)
