student_grades = {
	'John': 85,
	'Emily': 92,
	'Michael': 78,
	'Sarah': 95,
	'David': 88
}

# 1.Print the names of students who have a grade above 90.

above_90 = False

for student, grade in student_grades.items():
    if grade > 90:
        print(f"{student} scores {grade}")
        
above_90 = True
        
if not above_90:
    print(f"No student above 90")

# 2.Average Score

totalScore = sum(student_grades.values())
average = totalScore/len(student_grades)
print(average)

# Add new

newStudent = input('Enter student name: ')
score = int(input('Add score: '))

student_grades[newStudent] = score
mutate = list(student_grades.items())
newEntry = mutate[-1]

print(f"New entry is {newEntry}")
print(student_grades)
