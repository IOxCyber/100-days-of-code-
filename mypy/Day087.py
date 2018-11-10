class Fruits: #Main class
    def __init__(self, price, color):
        self.price = price
        self.color = color

class Apple(Fruits): #subclass
    def place(self):
        print("Kashmeri") 
     
class Papaya(Fruits): #subclass
    def shape(self):
        print("Egg like")

var = Apple("100", "Red")

print(var.color,var.price)



"""
Inheritance provides a way to share functionality between classes. 
"""
