# x=int(input("Enter 1st number"))
# y=int(input("Enter 2nd number"))

# def sum(a,b):
#     sum=a+b
#     return sum

# print(sum(4,5))
# print(sum(6,7))
# print(sum(x,y))

# add=sum(9,8)
# print(add)

# #function to print Hello

# def hello():
#     return "Hello World"

# s=hello()
# print(s)

# #function to calculate average of 3 numbers
# x=int(input("Enter 1st number"))
# y=int(input("Enter 2nd number"))
# z=int(input("Enter 2nd number"))


# def avg3(a,b,c):
#     avg=(a+b+c)/3
#     return avg

# ans=avg3(x,y,z)
# print(ans)

# #WA function to print length of list


# l1=[1,2,3,4,5,6]
# l2=["Ben10","Spiderman","G-One","RDR"]
# def lf(list):
#     x= len(list)
#     return x

# print(lf(l1))
# print(lf(l2))


# #Function to print elements of list in single line

# def line(list):
#     for items in list:
#         print(items,end=" ")
    
# line(l1)
# print()
# print(line(l2))

#Function to find factorial of n

# n=int(input("Enter number to find factorial of: "))
# def fact(num):
#     i=1
#     m=1
#     while(i<=num):
#         m=m*i
#         i=i+1
#     ## print(m) 
#     return m
   

# print(fact(n))


# #Function to convert USD to INR

# usd=int(input("Enter currency in USD"))
# def con(usd):
#     nep=usd*134
#     return nep

# print(con(usd))

#Recursion - Repeatition of same function ongoing
# Calls same function repeatedly

# def show(n):
#     if(n==0):
#         return     ##return used for stopping the recursion(condition to stop recursion)
#     print(n)
#     n=n-1
#     show(n)
# #call stack and recursion
# # In this case, no two values are returned hence, return with none value doesnot affect

# show(5)

#Factorial Through Recursion
# def fac(n):
#     s=1
#     for i in range(1,(n+1)):
#         s=s*i
#     print(s)

# fac(5)

# def fact(n):
#     if(n==0 or n==1):
#         return 1 
#     return n*fact(n-1)
# print(fact(5))

""" In recursive function, its better to return the value and print it
rather than just printing it inside function 

We need to understand it must return a value like condition to stop the
 recusion as it returned 1 when reached to level of 0 or 1 
meawhile it must also return the value alongside before entering the 
end zone.
# """

# #Function to calculate sum of first 10 natural number
# def s(n):
#     if(n==0):
#         return 0
#     return n+s(n-1) 

# #In this case, two values are returning so it can't return null value at last
# print(s(10))



#Recursive Function to print elements of list
def reclist(list, idx):  # Define a recursive function with a list and an index (default = 0)
    if idx == len(list):  # Base case: Stop recursion when index reaches the length of the list
        return  # Exit the function
    print(list[idx])  # Print the current element at index `idx`
    reclist(list, idx + 1)  # Recursive call with the next index

# Define a list of religious names
list1 = ["God", "Allah", "Bhagwan"] 
reclist(list1,0)  # Call the function with the list






