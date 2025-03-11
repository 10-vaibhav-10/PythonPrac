# """Create a new file "practise.txt " using python. Add following:
#     Hi everyone
#     we are learning FILE I/O
#     using Java
#     I like programming in Python.
# """

# # f=open("practise.txt","x")  # X mode to open the text file
# f=open("practise.txt","w")  # W mode to write in the text file
# f.write("Hi everyone \n")
# f.write("we are learning File I/O\n")
# f.write("using Java\n")
# f.write("I like programming in Java\n")
# f.close()

# with open("practise1.txt","w") as fho:
#     fho.write("Hi everyone\nWe are learning FILE I/O\n ")
#     fho.write("using Java\nI like programming in Python")


# #WAF that replaces all occurrences of "java" with "python" in above file

# with open("practise.txt","r") as f:
#    data= f.read()

# new=data.replace("Java", "Python")
# print(new)

# with open("practise.txt","w") as f:
#    f.write(new)

#     ## Another Technique 
# f=open("practise.txt","r") 
# data=f.read()
# print(data)

# new=data.replace("Python","java")
# f=open("practise.txt","w")
# f.write(new)
# f.close()


# ## search if word "learning" exists in a file
# with open ("practise.txt","r") as f:
#    data=f.read()    # read data from the file and store in data 
#    if(data.find("learning")!=-1):
#       print("Found it")
#    else:
#       print("Not Found")



# ## Function to find in which line of file does the word "learning" occur first
# def findline():
#    word="learning"
#    data=True
#    line=1
#    with open("practise.txt","r") as f:
#       while data:
#          data=f.readline()
#          if(word in data):
#               print(line)
#          line=line+1
            
# findline()



# #From file containing numbers separated by comma,print count of even numbers

# with open("Numbers.txt","r") as f:
#    c=0   # to take count of the even values
#    data=f.read()
#    print(data)

#    #getting individuals numbers from file
#    num=data.split(",")
#    print(num)
#    for val in num:
#       if (int(val))%2==0:
#          print(int(val))
#          c=c+1
   
# print("Total number of even numbers: ", c)