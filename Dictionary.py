#Used to store data values in "key:value" format
#unordered, changeable and can't hold duplicate key

dict={
    "name":"Vaibhav",
    "age":22,
    "destination" :"Australia",
    "Course" : "Master of Data Analytics",
    "Module": ["AI","IOT"]
}
print(dict["destination"])
print(dict)

dict["name"]="Rahul"
print(dict["name"])
print(dict)