# OOP Concepts
class Car:      ## Created Classe
    color="Blue"        ##Attributes
    brand="Mercedes"    ## Class instance

car1=Car()      # Object    
print(car1.color, car1.brand)


# __init__ Function ( Constructor )

class Student:
    college_name="Herald College"
## Here college_name is class instance that means it is same for every object 
    def __init__(self,name,marks):
            self.name=name
            self.marks=marks
            print("Adding new student.")
            
    def welcome(self):     ## method inside a class
        print("Welcome, ",self.name)

s1=Student("Rahul",88) # This calls the constructor at first.
s1.welcome()
print(s1.name,s1.marks)

#name,marks are object instance that varies according to object values.

s2=Student("Raj",98) # This calls the constructor at first.
print(s2.name,s2.marks)

"""Create student class that takes name and marks of 3 subjects as
arguments in constructor. Create method to print average."""
class Stud:
    def __init__(self,name):
         self.name=name
         

    def avg(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
        total=(m1+m2+m3)/3
        return total
        

stud1=Stud("Vaibhav")
print(stud1.name,"\t")
print("Average Marks obtained",stud1.avg(87,88,89))


#Create account with 2 attributes - balance and account no. // Create methods for debit,credit and printing the balance
class Bank:
    
    def __init__(self,balance,acc_no):
        self.balance=balance
        self.acc_no=acc_no
        
    def credit(self,c):
        print("Total amount credited is ", c)
        self.balance=self.balance+c
        print("Total Amount is: ",self.get_balance())
    
    def debit(self,d):
        print("Total amount debited is ",d)
        self.balance=self.balance-d
        print("Total Amount is: ",self.get_balance())
    
    def get_balance(self):    ##printing the amount
        
        return self.balance
    
    
    
customer=Bank(500000,3330100023777010) 
print("Account no:",customer.acc_no)
print("Amount: ",customer.balance)
customer.debit(50000)
customer.credit(5000)
print("You account has total of ",customer.get_balance())
