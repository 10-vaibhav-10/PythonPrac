# #LOOP IN python

# n=0
# while(n<5):
#     print("Hey there")
#     n=n+1


# #Print numbers from 1 to 100 and 100 to 1
# i=1
# while i<=100:
#     print("From 1 to 100: ",i)
#     i=i+1

# a=100
# while a>=1:
#     print("From 100 to 1: ",a)
#     a=a-1

# #Multiplication table of number n.
# tab=int(input("Enter a number: "))
# a=1
# while(a<=10):
#     m=tab*a
#     print(tab,"x",a,"=",m)
#     a=a+1

# #Print elements of following list using tuples
# list=[1,4,9,16,25,36,49,64,81,100]

# i=0
# x=len(list)
# print("Length of list: ",x )
# print("Listed Loop Started")
# while(i<x):
#     print(list[i])
#     i=i+1

#search for number in X in this tuple using loop
tup=(1,4,9,16,25,36,49,64,81,100)
y=len(tup)
print("Total number of data in tuple:" ,y)
i=0
find=int(input("Enter your number: "))

while i<y:  
    if(find==tup[i]):
            print("Your searched number is",find,"located in",i+1)
            break
                          
    i=i+1
    
else:
        print("Not Found")

    

    


    
     
