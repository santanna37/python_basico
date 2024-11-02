msg ='Welcome  to  Python  101: Split and Join'
csv = 'Eric,John,Michael,Terry,Graham'
friends_list = ['Eric','John','Michael','Terry','Graham']
# print(msg.split())
# print(msg.split(' '))

# print(msg)
# print(''.join(msg))
# print(''.join(msg.split()))

# print(' '.join(friends_list))



csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
friends_list = []
print(friends_list)
# From the list above fill a list(friends_list) properly
# with the names of all the friends. One per "slot"
# you may need to run same command several times
# use print() statements to work your way through the exercise
csv = csv.replace(':',',').replace(';',',')
friends_list = csv.split(',')
print(friends_list)

