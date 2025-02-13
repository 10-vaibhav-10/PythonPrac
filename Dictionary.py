#Used to store data values in "key:value" format
#unordered, changeable and can't hold duplicate key

dict={
    "name":"Vaibhav",
    "age":22,
    "destination" :"Australia",
    "Course" : "Master of Data Analytics",
    "Module":{
        "AI":56,
        "IOT":76,
        "Big Data":56
    }
    
}
print(dict["destination"])
print(dict)

dict["name"]="Rahul"
print(dict["name"])
print(dict)
print(dict["Module"]["IOT"])

#Dictionary Methods

print(dict.keys())  #keys used in dictionary formation

print(dict.values())    #returns value for the keys

print(dict.items())   #returns keys along value

print(dict["name"])
#Returns value for given key
print(dict.get("Destination"))  

#update/insert file to dictionary
#we need to create new dictionary variable and then
#update it to the old dictionary.
dict1={"name":"Ram ","gender":"male"}
dict.update(dict1)
print(dict) 