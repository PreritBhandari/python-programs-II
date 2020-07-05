"""
Write a Python class to find the three elements that sum to zero from a list of n real numbers.
Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
Output : [[-10, 2, 8], [-7, -3, 10]]
"""
new_list = []
arr = [-25, -10, -7, -3, 2, 4, 8, 10]
n=len(arr)
for i in range(0, n-2): 
    for j in range(i+1, n-1): 
        for k in range(j+1, n): 
            if (arr[i] + arr[j] + arr[k] == 0): 
                new_list.append([arr[i], arr[j], arr[k]])
print(new_list)
