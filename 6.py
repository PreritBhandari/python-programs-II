"""
Create a list with the names of friends and colleagues. Search for the
name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.
"""
def find_name(input_list):
    for each in input_list:
        if each=='John':
            return f'Found'
    return f'Not Found'
    
if __name__ == "__main__":
    print(find_name(["Rochak", "Abhishek","Rahul","Sudip","Sumir","Sumit","Sujan"]))