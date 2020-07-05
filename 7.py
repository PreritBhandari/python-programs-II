"""
Create a list of tuples of first name, last name, and age for your friends and colleagues. 
If you don't know the age, put in None.Calculate the average age, skipping over any None values. 
Print outeach name, followed by old or young if they are above or below the average age.
"""
list_profile=[("Ravi","Poudel",25),("Ram","Po",22),("Sam","Poudel",None),("Hari","Bahadur",21),("Madan","Shrestha",None)]
collect_age = [each[2] for each in list_profile if each[2] is not None]
avg_age=sum(collect_age)/len(collect_age)
print (f'average age is {avg_age}')
for each in list_profile:
    if each[2] is not None:
        if each[2] > avg_age:
            print(f'{each} is old')
        else:
            print(f'{each} is young')
    else:
        print(f'{each} has no age to determine')

