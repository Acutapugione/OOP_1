class Base:
    count: int = 0 #class property
    
    @classmethod 
    def show_count(cls):
        print(cls.count)
  
    def __init__(self, name, color) -> None: # object's method
        Base.count += 1
        self.name = name # object's property
        self.color = color # object's property
    
    def __del__(self):
        Base.count -= 1


b = Base("Jhon", "White")
a = Base("Jhon", "White")
c = Base("Jhon", "White")
d = Base("Jhon", "White")
b = Base("Jhon", "White")
# b = Base.__new__(Base)  #Так не робимо! Це не красиво!
# b.__init__()

# b.help_me()
# Base.help_me(b) #Так не робимо! Це не красиво!

b.show_count()
Base.show_count()
# print( id(total))
# import math
# import p_2
# print( id(math))
# print( id(p_2))
