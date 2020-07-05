"""
Imagine you are designing a banking application. What would a customer look like? What attributes would 
she have? What methods would she have?
"""
import datetime
class Customer:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
        self.balace = 0
    def get_balance(self):
        return self.balace

    def initial_amt(self):
        self.current_amt=1000
        return self.current_amt

    def after_payment(self,spent_amt):
        if self.balace - spent_amt > 0:
            self.balace -= spent_amt
        else:
            print (f'Not Enough Amt')

    def add_ammount(self,add_amt):
        self.balace+=add_amt
    def __str__(self):
        return f'{self.name},{self.age},{self.address}'

if __name__ == "__main__":
    obj=Customer("Rochak",20,"Koteshwor")
    print(obj)
    print(obj.get_balance())
    obj.add_ammount(100)
    print(obj.get_balance())
    obj.after_payment(200)
    obj.after_payment(20)
    print(obj.get_balance())

    

        
        


    
