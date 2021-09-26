dictionary= {

}
while True:
    word = input('\n\nFor translation use form: \'translation [word]\'\nFor add word use form\'Add [english word] [translation]\n\nWrite here\n')
    w = word.lower().split(' ')
    
    #perevod
    if w[0] == 'translation' and len(w) == 2:
        if w[1] in dictionary:
            print('\n\n',dictionary[w[1]])
        elif w[1] in dictionary.values():
            for x,y in dictionary.items():
                if y == w[1]:
                    print('\n\n',x)
        else:
            print('\n\nUnknown word')
    
    #dobavlenie
    elif w[0] == 'add' and len(w) == 3:
        if w[2] in dictionary:
            print('\n\nThe dictionary knows this word')
        elif w[2] in dictionary.values():
            print('\n\nThe dictionary knows this word')
        elif w[1] in dictionary:
            print('\n\nThe dictionary knows this word')
        elif w[1] in dictionary.values():
            print('\n\nThe dictionary knows this word')
        else:
            dictionary[w[1]] = w[2]
    else: 
        print('\n\nUnknown form')
