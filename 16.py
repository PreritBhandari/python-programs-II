"""
Imagine you are creating a Super Mario game. You need to define a class to represent Mario.
What would it look like? If you aren't familiar with SuperMario, use your own favorite video or board
game to model a player.
"""
class SuperMario:
    def __init__(self,color):
        self.color = color
        self.x = 0
        self.y = 0

    def move_ahead(self,unit):
        self.x = self.x + unit
    def jumpup(self):
        self.y =self.y + 1

    def current_position(self):
        return f'x-position:{self.x} and y-position:{self.y}'
    def go_down(self):
        if self.y > 0:
            self.y += 1
        else :
            print('You are Level 0')

obj=SuperMario('red')
obj.move_ahead(5)
print(obj.current_position())
obj.jumpup()
print(obj.current_position())

    

        

     
    
