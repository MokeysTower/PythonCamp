

class Airplane:
    maxSeats = 3
    
    def __init__(self,ID):
        self.ID= ID
        self.seats = []

class User: 
    ban = False
    
    def __init__(self,name,ID):
        self.ID = ID
        self.selfname = name
    
    def switchBan(self):
        self.ban = True

class Airport:
    airplanepark = []

    def addplane(self,x):
        self.airplanepark.append(x)
    
    def reserved(self,ID2,user):
        for plane in self.airplanepark:
            if plane.ID == ID2:
                if len(plane.seats) >= plane.maxSeats:
                    print('Error: this plane is full')
                elif 0<= len(plane.seats) < 3 and not user.ban: 
                    plane.seats.append(user)
                    print('\n\nSeat reserved\n\n')
                else:
                    print('Almostly this person baned')
        if user.ID != ID2:
            print('\n\nUncorrect ID\n\n')
    
    def unreserved(self,ID2,name):
        for plane in self.airplanepark:
            if plane.ID == ID2:
                for i in range(len(plane.seats)):
                    seaters = plane.seats[i]
                    if seaters.selfname == name:
                        plane.seats.pop(i)
                        print('\n\nSeat unreserved')
                        break
                if seaters.selfname == name:
                    break
                elif seaters.selfname != name:
                    print('\n\nThis person did\'t reserve on this plane')
                    break
        if plane.ID != ID2:
            print('\n\nThis plane not found\n')

    def showPlaneInfo(self,ID2):
        for plane in self.airplanepark:
            if plane.ID == ID2:
                print('\n\nID of plane: ',plane.ID,'\nSeater reserved on this plane:')
                try:
                    for i in plane.seats:
                        print('\nName:', i.selfname.title(),' ID:', i.ID )
                except:
                    pass
                break
        if plane.ID != ID2:
            print('\n\nThis plane not found\n')
                    



class UserList:
    users=[]

    def adds(self,x):
        self.users.append(x)
        print('\n\n',x.selfname.title(), ' added')
    
    def ban2(self,ID2):
        for user in self.users:
            if user.ID == ID2:
                print('\n\n', user.selfname.lower().title(),' baned.\n\n')
                user.switchBan()
        if user.ID != ID2:
            print('\n\nUncorrect ID\n\n')
    
    def find(self,ID2):
        for user in self.users:
            if user.ID == ID2:
                print('\nID: ',user.ID,' Name: ', user.selfname.title(),' Ban status: ', user.ban,'\n')
        if user.ID != ID2:
            print('\n\nUncorrect ID\n\n')

    #func for reservation
    def search(self,ID2):
        for user in self.users:
            if user.selfname == ID2:
                return user
        if user.selfname != ID2:
            print('\n\nUncorrect name of person\n\n')

    def alfind(self,ID2):
        for user in self.users:
            if user.selfname == ID2:
                print('\nID: ',user.ID,' Name: ', user.selfname.title(),' Ban status: ', user.ban,'\n')
        if user.selfname != ID2:
            print('\n\nUncorrect name\n\n')



class Main:
    u = UserList()
    IDcounterUser = 0

    def suck(self):
        x = input('\nFor add user write:\'add [name]\'\nFor ban user write:\'ban [ID of user]\'\nFor find the name of user by ID write:\'find [ID user]\'\nFor find the ID of user by name write:\'alfind [name]\'\n\nIf you want work with airplanes and reserve seats write:\'worklist\'\n').lower()
        if x.split(' ')[0] == 'add':
            self.IDcounterUser += 1
            y = User(x.split(' ')[1].lower(),self.IDcounterUser)
            self.u.adds(y)
        elif x.split(' ')[0] == 'ban':
            self.u.ban2(int(x.split(' ')[1]))
        elif x.split(' ')[0] == 'find':
            self.u.find(int(x.split(' ')[1]))
        elif x.split(' ')[0] == 'alfind':
            self.u.alfind(x.split(' ')[1].lower())
        elif x.split(' ')[0] == 'worklist':
            while True:
                x = input('\n\nFor reserve seat write:\'reserve [ID of airplane] [Name of person]\'\nFor unreserve seat:\'unreserve [ID of plane] [Name of person]\'\nFor find the info about plane write:\'infoplane [ID of plane]\'\nFor back to previous menu write:\'back\'\n').lower()
                if x.split(' ')[0] == 'reserve':
                    airport.reserved(int(x.split(' ')[1]), self.u.search( x.split(' ')[2] ))
                elif x.split(' ')[0] == 'unreserve':
                    airport.unreserved(int(x.split(' ')[1]), x.split(' ')[2] )
                elif x.split(' ')[0] == 'infoplane':
                    airport.showPlaneInfo(int(x.split(' ')[1]))
                elif x.split(' ')[0] == 'back':
                    break
                else:
                    print('\n\nUnknown command\n\n')
        elif x.split(' ')[0] == 'out':
            print('\n\nGoodbye!\n\n')
            return 1
        else:
            print('\n\nUnknown command\n')

IDcounterAirplane = 0
z = Main()
airport = Airport()

#loop of input count of airplane
while True:
    try:
        x = input('How many airplanes we have?')
        for i in range(int(x)):
            IDcounterAirplane += 1
            airport.addplane(Airplane(IDcounterAirplane))
        print(f'Create {int(x)} planes')
        break
    except:
        print('\nWrite correct number without letters\n')
    

while True:
    y = z.suck()
    if y == 1:
        break
