#built in data type that create immutable sequence 
# immutable - value can't be changed

tup=(2,3,4,5,6,7,8,9)

print(type(tup))

#access value through index
print(tup[2])
#but this is not allowed like "tup[0]=5" 

 
tup=("Hi","Hey",1,2,4.55,5.66,2)
print(tup)

#methods in tuple

#find first element in tuple
print(tup.index(2))

#repeatition of data in tuple
print(tup.count(2))