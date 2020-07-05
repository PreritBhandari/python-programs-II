"""
Create a list. Append the names of your colleagues and friends to it.
Has the id of the list changed? Sort the list. What is the first item on
the list? What is the second item on the list?
"""
list_name=['Prerit']
print(f'id of new list{list_name} :{id(list_name)}')
list_name.append('Ravi')
print(f'id of 2nd append list{list_name}: {id(list_name)}')
list_name.append('Pragyan')
print(f'id of 3rd append {list_name}:{id(list_name)}')
list_name.sort()
print(f'Sorted list is:{list_name}')
print(f'the second item on thelist is {list_name[1]}')
