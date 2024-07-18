### Dictionary ###

item1 = {'name':'mojjam', 'age': 32, 'address': 'lagos'}
item2 = {'name':'professor', 'age': 42, 'address': 'ibadan'}
item3 = {'name':'ujunwa', 'age': 52, 'address': 'delta'}

names = [item1, item2, item3]
print(names)

details = 'My name is', item1.get('name'), ', I am', item1.get('age'), 'years old, I live', item1.get('address')
print(str(details))

## Assignment ##

student_grades = {
	'John': 85,
	'Emily': 92,
	'Michael': 78,
	'Sarah': 95,
	'David': 88
}

# 1.Print the names of students who have a grade above 90.
for grade in student_grades.values():
    if grade > 90:
        print(grade)
        
# 2.Calculate the average grade of all students.
from operator import *

average = 0

#for grade in student_grades.values():
#    average = add(grade, average)
#print(average)

# 3.Add a new student to the dictionary with a grade of 80.

student_grades['Mariam'] = 80
print(student_grades)
    
for grade in student_grades.values():
    average = add(grade, average)
print(average)
