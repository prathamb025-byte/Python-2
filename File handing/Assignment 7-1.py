#write the file
file=open("my_file.txt","w")
file.write("Hello Students")
file.close()

#append file
file=open("my_file.txt","a")
file.write("\nWelcome to python")
file.close()

#read file
file=open("my_file.txt","r")
data=file.read()
print(data)
file.close

