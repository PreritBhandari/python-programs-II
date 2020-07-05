"""
Write a binary search function. It should take a sorted sequence and
the item it is looking for. It should return the index of the item if found.
It should return -1 if the item is not found.
"""
def bin_search(list_no,n):
    while True:
        mid = len(list_no)//2
        try:
            if n < list_no[mid]:
                list_no=list_no[:mid]
            elif n > list_no[mid]:
                list_no=list_no[mid:]
            elif  n== list_no[mid]:
                return f'It is in index {listNumber.index(n)} in input list'
        except IndexError:
            return 'Error :-1'

if __name__ == "__main__":
    listNumber=[7,8,1,3,4,6,2,5,9]
    takeInput=int(input('Enter no'))
    print(bin_search(sorted(listNumber),takeInput))
