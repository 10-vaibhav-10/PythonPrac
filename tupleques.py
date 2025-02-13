#Append movies name in a list
list=[]     #indicates list named variable is list dt
a=input("Enter fav movie name")
b=input("Enter fav movie name")
c=input("Enter fav movie name")

# l=[a,b,c]
# print(l)

list.append(a)
list.append(b)
list.append(c)
print(list)

#WAP to check if a list contains palindrome of elements.

list1=[1,2,3,4]
list2=[3,2,1,4]
list3=[4,3,3,4]

x=list1.copy()
x.reverse()

y=list2.copy()
y.reverse()


z=list3.copy()
z.reverse()


if(list1==x):
    print("First list is palindrome.")
elif(list2==y):
    print("Second list is palindrome.")
elif(list3==z):
    print("3rd list is palindromec")    

#WAP To count number of students with "A" grade
#   ["C","D","A","A","B","B","A"]

x=("C","D","A","A","B","B","A")

print("Number of A in this tuple is: ", x.count("A"))

#Store above values in list and sort them.
Val=[]

Val.append(x[0])
Val.append(x[1])
Val.append(x[2])
Val.append(x[3])
Val.append(x[4])
Val.append(x[5])
Val.append(x[6])
print(Val)

Val.sort()
print("Sorted values in Val list: ", Val)



