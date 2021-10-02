#Dictioinary letters from Morse
z = {'.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F','--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L','--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R','...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X','-.--':'Y','--..':'Z','.----':'1','..---':'2','...--':'3','....-':'4','.....':'5','-....':'6','--...':'7','---..':'8','----.':'9','-----':'0'}

def decoding(q):
    global z
    global t
    q= str(q)
    f = q.split(' ')
    for i in range(len(f)):
        t += z[f[i]]
    return

x = input('Rules:\n[Word] 3xSpaces [Word]\n[Letter] Space [Letter]\n\nExample:\'.... . .-.. .-.. ---   .- -. -.\' -> \'HELLO ANN\'\n\nWrite code\n')
# takes words
y = x.split('   ')
#this is our final message
t = ''
for i in range(len(y)):
    decoding(y[i])
    t += ' '
if t[len(t)-1] == ' ':
    t = t[:-1]
print(t)