"""
Write code that will print out the anagrams (words that use the same letters) from a paragraph of text.
"""
ip_para=['cat','dog','act','tac','god']
sorted_list=[]
find_index=[]
group=[]
sort= lambda x:sorted(x)
for each in ip_para:
    sorted_list.append(sort(list(each)))
# print(sorted_list)
sorted_list=[''.join(each) for each in sorted_list]
set_sorted=set(sorted_list)
for each in set_sorted:
    group=[]
    if sorted_list.count(each)>1:
        find_index=[index for index, value in enumerate(sorted_list) if value == each]
        for i in find_index:
            group.append(ip_para[i])
        print(group)


