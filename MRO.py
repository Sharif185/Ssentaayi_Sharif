class User:
    def get_role(self):
        print("I am a general user.")

class Instructor(User):
    def get_role(self):
        print("I am an instructor.")

class Student(User):
    def get_role(self):
        print("I am a student.")

class TeachingAssistant(Instructor, Student):
    pass

# Create a Teaching Assistant
ta = TeachingAssistant()
ta.get_role()

# Show MRO
print(TeachingAssistant.__mro__)
