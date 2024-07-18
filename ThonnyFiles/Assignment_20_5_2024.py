## Assignment 1 ##

student_grades = {
	'John': 85,
	'Emily': 92,
	'Michael': 78,
	'Sarah': 95,
	'David': 88
}

# 1.Print the names of students who have a grade above 90.
from operator import *

total = 0

for grade in student_grades.values():
    total += grade
    if grade > 90:
        print(grade)

        
# 2.Calculate the average grade of all students.

from operator import *

aver = 0

for grade in student_grades.values():
    average = average(grade, aver)
print(average)

# 3.Add a new student to the dictionary with a grade of 80.
student_grades['Mariam'] = 80
print(student_grades)

## Assignment 2 ##

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

#1. Find the intersection of set1 and set2 (elements common to both sets).

#2. Find the union of set1 and set2 (all elements from both sets).

#3. Find the difference of set1 and set2 (elements in set1 but not in set2).