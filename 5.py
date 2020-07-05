"""
Create a tuple with your first name, last name, and age. Create a list, people, and append your tuple to 
it. Make more tuples with the corresponding information from your friends and append them to the list. 
Sort the list. When you learn about sort method, you can use the key parameter to sort by any field in 
the tuple, first name, last name, or age.
"""
def find_name(input_list):
    list_info.append(input_list)
    return list_info
if __name__ == "__main__":
    list_info=[("prerit","bhandari",20)]
    for i in range(2):
        name = input('Enter Your Name')
        lastName = input('Enter Your Last Name')
        age = int(input('Enter Your Age'))
        make_tuple = (name,lastName,age)
        print(find_name(make_tuple))
    print(f'Sort Using Name{sorted(list_info,key=lambda x: x[0])}')
    print(f'Sort Using Lastname{sorted(list_info,key=lambda x: x[1])}')
    print(f'Sort Using Age{sorted(list_info,key=lambda x: x[2])}')
