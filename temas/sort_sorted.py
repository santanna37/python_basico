""" 
# SORTED => quando quiser uma nova lista ordenada sem modificar a original 
# SORT => quando quiser ordenar a lista original 

* tuplas tem regras com alterações 
"""

my_list = [1,5,3,7,2]
my_dict = {'car':4,'dog':2,'add':3,'bee':1}
my_tuple = ('d','c','e','a','b')
my_string = 'python'

# Sort list
print(my_list,'original')
print(my_list.sort(),'sort') # não da retorno, mas organza a lista
print(my_list,'sort')
print(my_list.reverse(), 'reverse') # não tras retorno, mas inverte a ordem 
print(my_list, "reverse")
print(sorted(my_list),"sorted") # organiza a lista com retorno 
print(sorted(my_list, reverse=True), 'sorted, reverse') # organiza decresente com retorno 

# reversed list 

print(list(reversed(my_list)), 'lista com reversed') # organiza de forma decresente  
print('================================================================')

# Sort tupla
print(my_tuple,'original')
#print(my_tuple.sort(),'sort') # não da retorno, mas organza a lista
#print(my_tuple,'sort')
#print(my_tuple.reverse(), 'reverse') # não tras retorno, mas inverte a ordem 
#print(my_tuple, "reverse")
print(sorted(my_tuple),"sorted") # organiza a lista com retorno 
print(sorted(my_tuple, reverse=True), 'sorted, reverse') # organiza decresente com retorno 

print('================================================================')


# Sort str
print(my_string,'original')
#print(my_string.sort(),'sort') # não da retorno, mas organza a lista
#print(my_string,'sort')
#print(my_string.reverse(), 'reverse') # não tras retorno, mas inverte a ordem 
#print(my_string, "reverse")
print(sorted(my_string),"sorted") # organiza a lista com retorno 
print(sorted(my_string, reverse=True), 'sorted, reverse') # organiza decresente com retorno 

print('================================================================')


# Sort Dict
print(my_dict,'original')
#print(my_dict.sort(),'sort') # não da retorno, mas organza a lista
#print(my_dict,'sort')
#print(my_dict.reverse(), 'reverse') # não tras retorno, mas inverte a ordem 
#print(my_dict, "reverse")
print(sorted(my_dict),"sorted") # organiza a lista com retorno
print(sorted(my_dict.items()),' sordted por .item()')
print(sorted(my_dict.values()),"serted com .values()") # organiza pelos valores  
print(sorted(my_dict, reverse=True), 'sorted, reverse') # organiza decresente com retorno 
print(sorted(my_dict.values(), reverse= True), 'sorted com values e reverse = true ')
print('================================================================')