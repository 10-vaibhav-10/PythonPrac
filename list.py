#working with list and tuples
# can list any amount of data and seperated by ","

marks=[89,88,87,84,85]
print("Total data inside array: ",len(marks))
print("3rd Index value is: ",marks[3])

#in list we can store any types together
student=["Ram",1,"Male",17]
print(type(student))
print(student)

#Value can be changed in list
student[0]="Hari"
print(student)

#slicing in list gets from starting index 
# to the index before it ends
print(student[1:3])

student.append("Butwal")    #adds element to the end of the list
#only similar type of data can be sorted
   #so we made the student list to be string
l=['a','e','d','c','b','f']
l.sort() #sort in ascending order
print(l)
# sort in descending order
l.reverse()
print(l)

l.insert(0,"Ben10")   #insert element at a specific index
print(l)

l.remove('e')   #remove first found specific element
print(l)

l.pop(3)    #remove the element found in specific index of the list
print(l)

