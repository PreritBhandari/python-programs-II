"""
Write a Python class to find validity of a string of parentheses, '(',
')', '{', '}', '[' and ']. These brackets must be close in the correct order,
for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid
"""

def parenthese(str1):
        stack  = []
        all_ip =  {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
            if parenthese in all_ip:
                stack.append(parenthese)
            elif len(stack) == 0 or all_ip[stack.pop()] != parenthese:
                return f'Invalid'
        return f'Valid'

print(parenthese("(){}[]"))
print(parenthese("()[{)}"))
print(parenthese("()"))
print(parenthese("({(}))"))