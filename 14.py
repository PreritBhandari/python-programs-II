"""
Write a function that reads a CSV file. It should return a list of dictionaries, using the first row
as key names, and each subsequent row as values for those keys. For the data in the previous example it
would return:
[{'name': 'George', 'address': '4312 Abbey Road', 'age': 22}, {'name':
'John', 'address': '54 Love Ave', 'age': 21}]
"""
import csv
def read_file():
    create_dict={}
    with open('profile.csv','r') as file:
        reader_value = csv.reader(file)
        reader_value_list=list(reader_value)
        for i in range(1,len(reader_value_list)):
            create_dict[reader_value_list[0][0]]=reader_value_list[i][0]
            create_dict[reader_value_list[0][1]]=reader_value_list[i][1]
            create_dict[reader_value_list[0][2]]=reader_value_list[i][2]
            print(create_dict)
if __name__ == "__main__":
    read_file()