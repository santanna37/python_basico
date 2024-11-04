#Sets - Exercise

#1. Check if ‘Eric’ and ‘John’ exist in friends
#2. combine or add the two sets 
#3. Find names that are in both sets
#4. find names that are only in friends
#5. Show only the names who only appear in one of the lists
#6. Create a new cars-list without duplicates

friends = {'John','Michael','Terry','Eric','Graham'}
my_friends = {'Reg','Loretta','Colin','John','Graham'}
cars =['900','420','V70','911','996','V90','911','911','S','328','900']

#1. Check if ‘Eric’ and ‘John’ exist in friends
print(f" John exist in friends? {'John' in friends} ")
print(f"Eric exist in friends?{'Eric' in friends}")
print(f"John and Eric exists in friends? {'John' and 'Eric' in friends}")

#2. combine or add the two sets 
new_friends = friends.union(my_friends)
print(new_friends)

#3. Find names that are in both sets
same_friends = friends.intersection(my_friends)
print(same_friends)

#4. find names that are only in friends
unique_friends = friends.difference(my_friends)
print(unique_friends)

#5. Show only the names who only appear in one of the lists
only_friends = friends.difference(my_friends).union(my_friends.difference(friends))
print(only_friends)

#6. Create a new cars-list without duplicates
cars = list(set(cars))
print(cars)