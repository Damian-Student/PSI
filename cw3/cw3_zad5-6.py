############### definice klas #####################
class Calculator:
    def __init__ (self):
        print("Uruchomiono kalkulator")
    def add(self, x,y):
        print(x+y)
    def subtract(self,x,y):
        print(x-y)
    def multiply(self,x,y):
        print(x*y)
    def divide(self,x,y):
        print(x/y)

class ScienceCalculator(Calculator):
    def __init__ (self):
        print("Uruchomiono kalkulator naukowy")
    def square(self, x):
        print(x*x)
    def cube(self,x):
        print(x*x*x)

###################################################
# realizacja
calc = Calculator()
calc.add(4,5)
calc.subtract(8,2)
calc.multiply(3,4)
calc.divide(9,3)
calc = ScienceCalculator()
calc.square(4)
calc.cube(2)