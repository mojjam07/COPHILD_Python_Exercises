# Reading from a  file

with open('text.txt') as file_object:
    contents = file_object.read()
print(contents)

with open('text.txt') as file_object:
    contents = file_object.read()
print(contents.lstrip())

# Reading line by line

filename = 'text.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
        
# Making a list of lines from a file

with open('text.txt') as file_object:
    lines = file_object.readlines()
    
for line in lines:
    print(line.rstrip())
    
# Working with a file's contents

filename = 'text.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.rstrip()
    
print(pi_string)
print(len(pi_string))
    
# Large files: One Million Digits

filename = 'text.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.rstrip()
    
print(f"{pi_string[:18]}.....")
print(len(pi_string))

# Write to a file

filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write('I am writing to a file.')
    

# Writing Multiple lines

filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write('I love programming.\n')
    file_object.write('I love creating new games.\n')

# Appending to a file

filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write('I also love finding meaning in large dataset.\n')
    file_object.write('I love creating apps that can run in browser.\n')