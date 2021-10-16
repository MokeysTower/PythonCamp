class Car:
    currentspeed = 0
    isride= False
    def __init__(self,brand,model,maxspeed):
        self.brand = brand
        self.model = model
        self.maxspeed = maxspeed

    def setSpeed(self,x):
        self.currentspeed = x
    
    def switchEngine(self):
        self.isride = not self.isride

r = input('\n\n\nDescribe car:\'brand model maxspeed\'\n').split(' ')
y = Car(r[0],r[1],r[2])
while True:
    r = input('Choose achion:\n\'Out\'\n\'Switch engine\'\n\'Choose speed [speed]\'\n').lower().split(' ')
    if r[0] == 'out':
        print('\n\nGame over!\n\n'.upper())
        break
    elif r[0] == 'switch':
        y.switchEngine()
        continue
    elif r[0] == 'choose':
        if r[2] > y.maxspeed:
            print('Uncorrect speed')
            continue
        else: 
            y.setSpeed(r[2])
    else:
        print('Uncorrect command')
        

