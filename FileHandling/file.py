f=open("File Handling\Text.txt","r")

lin1=f.readline()
print(lin1)
specific=f.read(10)
print(specific) #prints only 10 characterss

lin2=f.readline()
print(lin2)

##as all data has been ready by readline, it does not present data read from read().
data=f.read()
print(data)

f.close()


f=open("File Handling\Try.txt","w")

f.write("Hey, it is working now as it overwrites previous data though ""write"" mode\n")
print("This overwrites previous data though ""write"" mode")
f.close()

f=open("File Handling\Try.txt","a")

f.write("Hey, it is working now as it append data through ""append"" mode\n")
print("This adds data data through ""append"" mode")
f.close()