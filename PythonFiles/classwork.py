class Person:
    def __init__(self, name, age, gender) -> None:
        self.name = name
        self.age = age
        self.gender = gender

class Student(Person):
    def __init__(self, name, age, gender, level, school) -> None:
        super().__init__(name, age, gender)
        self.level = level
        self.school = school
    
    def __str__(self) -> str:
        return f"My name is {self.name}, {self.gender} and {self.age} years old. I'm a student of {self.school} currently in {self.level}level"


me = Student('Ayo', 21, 'Male', 200, 'Uniben')
print(me)