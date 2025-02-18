#store following word meaning in python dictionary
#table:"furniture" ,"list of facts & Figures"
#cat: "small animals"


dict={}
dict.update({"Table": {"Furniture","List of facts"},"cat":"a small animal"})

print(dict)

#Given list of subjects are for students.Assume one classroom is required for 1 subject. How many classroom is needed for students.
#"python","java","C++","python","javascript","java","python","java","C++","C"

set={"python","java","C++","python","javascript","java","python","java","C++","C"}
print(set)
print("The total number of class to set is: "+ str(len(set)))

"""WAP to enter marks of 3 subjects from user and store them in 
dictionary. Start with empty dictionary and add one by one using 
name as key and value.
"""""

dic1={}
dic1.update({"AI":5})
dic1.update({"IOT":7})
dic1.update({"Big Data":10})
print(dic1)

#Store 9 and 9.0 as separate value in set
set={9,0,"9.0"}
set1={
    ("float",9.0),
      ("int",9)
      }
#one as string other in number value
print(set)
print(set1)


