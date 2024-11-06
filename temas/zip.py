nums = '1234' 
letters = ['a','b','c','d']
names =['John','Eric','Michael','Graham','Joe']
# combo = list(zip(nums,letters,names))
# print(combo)
# num,let,nam =zip(*combo)
# print(num,let,nam)
nums = list(nums)
#print(list(nums))
combo = list(zip(nums,names))
print(combo)

combo = list(zip(nums,names,letters))
print(combo)


# dicionarios 
combo = dict(zip(nums, (*letters,*names)))
print(combo, ' teste')

combo = {num: (letters,names) for num, letters, names in zip(nums,letters,names )}
print(combo)
#combo = dict(zip(nums,names,letters))
print(combo)