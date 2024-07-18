# creating of a file ......... .txt


# step 1: open the file for any mode 'w, r, & a'
file_reader = open("file1.txt", "r")

# step 2: read or write the content
content = file_reader.read()
#content = file_reader.write('\n---- sodaqqallahul azeem ----') # where to write to file1.txt
print(content)
print(len(content))

# step 3: close the file
file_reader.close()