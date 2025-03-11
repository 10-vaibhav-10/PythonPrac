# class Account:
#     def __init__(self,acc_no,pw):
#         self.acc_no=acc_no
#         self.__pw=pw      ## we cant provide this aspect of attribute to public. So it must be made private just by adding __ before the attribute
      
#     def reset_pw(self):
#         print(self.__pw) ## it is accessed within class method
        
# ac=Account("3330100023777010","Vaibhav123@")
# print(ac.acc_no)
# ac.reset_pw()       ## accessed from a method of the class but not directly.

## Another class

class Person:
    __name="Who"    # set as private attribute here
    
    def __init__(self,gender):
        self.__gender=gender
    
    def sex(self):
        print(self.__gender)
        
    def __orientation(self):        # The method is hidden now as private method
        print("LGQBT+++++++")
        
    def Orientation(self):
       self.__orientation()  ## Accessing the __orientation private method through Orientation method.

p=Person("Other")
p.Orientation() ## Accessing method that can access private method here
p.sex()     