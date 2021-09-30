hero = { 
    'health': 100,
    'damage': 10
}
Army = []
id = 0

def addSkeleton(z,q,y):
    global Army
    global id
    id += 1
    army1 ={'Name': z,'ID': id,'health':q,'damage':y}
    Army.append(army1)
    print('\n\nUnit added\n')
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
    if len(Army[x-1]) == 0:
        print('Skeleton with this ID dead or not exists\n')
        return
    #raunds
    while True:
        if hero['health'] <= 0:
            print('Hero dead')
            return
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
            if hero['health'] <= 0:
                currHealth = Army[x-1]['health']
                print(f'\n\nHero dead.\n\nSkeleton:\nHealth:{currHealth}\n')
                return
            currHealth = hero['health']
            currHealth2 = Army[x-1]['health']
            print(f'Hero:{ currHealth }\nSkeleton:{ currHealth2 }')


while True:
    print('\n\nFor create new unit write: \'add (name)\'\nFor delete unit write: \'add (ID)\'\nFor attack hero write: \'fight (ID)\'\nFor out write: \'out\'\n\n')
    v = input('What we wiil do?').lower()

    #add unit
    if v.split(' ')[0] == 'add':
        x = v.split(' ')[1]
        if len(v.split(' ')) == 2:
            addSkeleton(x,20,10)
        elif len(v.split(' ')) == 4:
            q = int(v.split(' ')[2])
            y = int(v.split(' ')[3])
            addSkeleton(x,q,y)
        else:
            print('Unknown characteristics')
        continue
    #find
    elif v.split(' ')[0] == 'find':
        x = int(v.split(' ')[1])
        print(alfind(x, Army))
        continue
    elif v.split(' ')[0] == 'fight':
        x = int(v.split(' ')[1])
        fight(x)
        continue
    elif v.split(' ')[0] == 'del':
        x = int(v.split(' ')[1])
        deletiSkel(x)
        continue
    elif v.split(' ')[0] == 'show':
        for i in range(len(Army)):
            print(Army[i])
    elif v.split(' ')[0] == 'out':
        break
