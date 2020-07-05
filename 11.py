"""
Create a variable, filename. Assuming that it has a three-letter extension, and using slice operations, 
find the extension. For README.txt, the extension should be txt. Write code using slice operations that
will give the name without the extension. Does your code work on filenames of arbitrary length?
"""
filename="README.txt"
print(f'The extension of the file is {filename[-3:]}')
print(f'The file name without extension is {filename[0:-4]}')


