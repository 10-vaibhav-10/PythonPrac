#set is collection of unordered items
#unordered means no index value
#set is mutable but its elements are not
#Items must be unique
#We can store list or dictionary in set as they can be changed.

set={1,2.2,2,2,3,"Hello",4.4,5,"Hello"}
print(set)
print(type(set))
#can print details randomly, follows no order.

print(len(set))
#even length ignore the duplicate values.

#Set Methods 
set.add("Hari")
print(set)

set.remove(4.4)
print(set)

#POP takes away the elements from given set
x=set.pop()
print(x)

print(set)

#clear just delete all the elements inside of set
set.clear()
print(set)

#set aspects

set1={1,2,3,4,5,6,7,8,9,10}
set2={2,4,6,8,10,12,14,16,18,20}

print(set1.union(set2))
print(set1.intersection(set2))



