f=open("File Handling\Try.txt","r+")
#r+ can read and overwrite. Pointer is in starting point
#w+ can truncate. - File data gets deleted.
#a+ read and append - no truncate. Pointer is in end 
f.write("Starting: ")
print(f.read)
f.close()

with open("Withopen.txt","w") as f:
    data=f.write("This file is created using (with) operation")
    print(data)