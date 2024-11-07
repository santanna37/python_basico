numbers = [1,2,3,4,5,6,7,8,9]
# give me a list with num squared for each num in numbers
new_list = []
for num in numbers:
    new_list.append(num*num)
print(new_list)

new_list = [num*num for num in numbers]
print(new_list)

new_list = [ num * num for num in numbers if num %2 == 0]
print(new_list)

