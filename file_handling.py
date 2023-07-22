
# The file f.txt will be opened with the reading mode.
# Then will print every line one by one in the file
f_file = open("f.txt", "r")
for line in f_file:
    print("line: ", line)

# To extract a string that contains all characters in the file then we can use file.read()
print (f_file.read())

# Reading a file using with()statement
with open("f.txt") as file: 
    data = file.read()  
print(data)

# Highly recommended to close the file once done using it
f_file.close()

# To write content into a file, Use the access mode "w" to open a file in a write mode.
new_text = "This is new content"
opened = open("file.txt", 'w')
# If a file already exists, it truncates the existing content
# and places the filehandle at the beginning of the file.
# A new file is created if the mentioned file doesn’t exist.
opened.write(new_text)
# If We want to add content at the end of the file, use the access mode "a" to open a file in append mode