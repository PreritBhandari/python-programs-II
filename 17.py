"""
Write a program that serves as a basic calculator. It asks for two numbers, then it asks for an operator. 
Gracefully deal with input that doesn't cleanly convert to numbers. Deal with division by zero errors.
"""
class Calculator:
    def __init__(self,paramOne,paramTwo):
        self.paramOne=int(paramOne)
        self.paramTwo=int(paramTwo)
    def add(self):
        return self.paramOne+self.paramTwo
    def mul(self):
        return self.paramOne*self.paramTwo
    def minus(self):
        return self.paramOne-self.paramTwo
    def division(self):
        try:
            return self.paramOne/self.paramTwo
        except ZeroDivisionError:
            return f'Cannot divide number by xero, change your second paramerter as non zero'
    # def __str__(self):
    #     return f'{self.result}'
if __name__ == "__main__":
    inputOne=input('Enter 1st  numbers')
    inputTwo=input('Enter Second No')
    obj=Calculator(inputOne,inputTwo)
    print(f'Addition:{obj.add()}')
    print(f'Substraction:{obj.minus()}')
    print(f'Multiplication:{obj.mul()}')
    print(f'Division:{obj.division()}')
    
    
