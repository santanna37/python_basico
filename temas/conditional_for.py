names = ['john ClEEse','Eric IDLE','michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']

def invite():
    lists = []
    lists.extend(names + names1)
    i = 's'
    i = str(input('You need adding more friends? s/n   ').lower())

    while i != 'n':
        lists.append(str(input('Digit the name to your friend: ').title()))
        i = str(input('you need adding more friends? s/n    ').lower())
    

    for friend in lists:
        print(f" Horne {friend.title()}, You are invited to the my party ! ")
        
invite()