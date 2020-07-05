"""
Write a function that takes camel-cased strings (i.e.
ThisIsCamelCased), and converts them to snake case (i.e.
this_is_camel_cased). Modify the function by adding an argument,
separator, so it will also convert to the kebab case
(i.e.this-is-camel-case) as well.
"""
def convert_to_snake(input_str):
    list_str=list(input_str)
    new_list=[]
    for i in range(len(list_str)):
        if i!=0 and list_str[i].isupper():
            new_list.append('_')
        new_list.append(list_str[i].lower())
    return ''.join(new_list)
    
def convert_to_kebab(input_str):
    list_str=list(input_str)
    new_list=[]
    for i in range(len(list_str)):
        if i!=0 and list_str[i].isupper():
            new_list.append('-')
        new_list.append(list_str[i].lower())
    return ''.join(new_list)

if __name__ == "__main__":
    inputStr=input('Input Camel Case String')
    print(convert_to_snake(inputStr))
    print(convert_to_kebab(inputStr))

