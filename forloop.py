# #for loop in python //list, tuple

# list=[1,2,3,4,5,6]

# for i in list:
#     print(i)

# game=["Ben 10","GTA V","RDR 2","Spiderman"]

# for g in game:
#     print(g)

# name="Vaibhav"

# for c in name:
#     if (c=="a"):
#         print("Found ",c)
    
# else:
#     print("End")

# #Print elements from given list using for loop
# ta=[1,4,9,16,25,36,49,64,81,100]

# for i in ta:
#     print(i)

# #search number in tuple using loop

# tup=(1,4,9,16,25,36,49,64,81,100)

# x=int(input("Enter number: "))
# for a in tup:
#     if(x==a):
#         print("Found the number: ",x)

# #Range in For Loop
# # Range starts from 0 to 
# for x in range(5):
#     print(x)

# print("New Range where starts from 1 goes to 10 and takes step of 3")
# #excludes the last step 
# #range(start,stop,step)
# for y in range(1,10,3):
#     print(y)

# #loop work
# #Print element of given list usign loop
# x=[1,4,9,16,25,36,49,64,81,100]

# for i in x:
#     print(i)

# #search for number x in tuple using loop.
# y=(1,4,9,16,25,36,49,64,81,100)
# check=int(input("Enter the number to check: "))

# c=0
# for a in y:
#     c=c+1
#     if(check==a):
#         print("Found the number in: ",c)

# #print multiplication table of number "n" using range
# ntm=int(input("Enter the number: "))
# for i in range(1,11):
#     print(ntm,"x",i,"=",ntm*i)

#pass is null statement that does nothing, used as placeholder for code

#To find sum of first n number
n=int(input("Enter a number: "))
s=0;i=1
while(i<=n):
    s=s+i
    i=i+1

print("Sum of total number leading to ",n, "is",int(s))


#Factorial of first n number using "for" loop
a=int(input("Enter a number: "))
s=1

for i in range(1,(a+1)):
    s=s*i

print("Factorial of the number",a,"is,",int(s))