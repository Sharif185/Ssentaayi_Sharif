from abc import ABC, abstractmethod

# Base Abstract Class (Person)
class Person(ABC):
    def __init__(self, name: str, age: int, email: str):
        self.__name = name  # Encapsulated attribute
        self.__age = age
        self.__email = email

    # Getters and Setters (Encapsulation)
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def age(self):
        return self.__age

    @property
    def email(self):
        return self.__email

    @abstractmethod
    def role(self) -> str:
        pass

    def __str__(self):
        return f"{self.__name}, {self.__age} years old, Email: {self.__email}"

# Subclass 1: Lecturer
class Lecturer(Person):
    def __init__(self, name: str, age: int, email: str, department: str, salary: float):
        super().__init__(name, age, email)
        self.__department = department
        self.__salary = salary  # Private attribute

    def role(self) -> str:
        return "Lecturer"

    def teach(self, course: str) -> str:
        return f"{self.name} is teaching {course} in {self.__department}."

    # Getter for salary (Encapsulation)
    @property
    def salary(self):
        return self.__salary

    def __str__(self):
        return f"{super().__str__()}, Department: {self.__department}"

# Subclass 2: Student
class Student(Person):
    def __init__(self, name: str, age: int, email: str, student_id: str, major: str):
        super().__init__(name, age, email)
        self.__student_id = student_id
        self.__major = major

    def role(self) -> str:
        return "Student"

    def study(self) -> str:
        return f"{self.name} is studying {self.__major}."

    @property
    def student_id(self):
        return self.__student_id

    def __str__(self):
        return f"{super().__str__()}, ID: {self.__student_id}, Major: {self.__major}"

# Subclass 3: Staff
class Staff(Person):
    def __init__(self, name: str, age: int, email: str, position: str):
        super().__init__(name, age, email)
        self.__position = position

    def role(self) -> str:
        return "Staff"

    def manage(self) -> str:
        return f"{self.name} is managing university resources as a {self.__position}."

    def __str__(self):
        return f"{super().__str__()}, Position: {self.__position}"

# Demo
if __name__ == "__main__":
    # Create instances
    lecturer = Lecturer("Dr. Smith", 45, "smith@uni.edu", "Computer Science", 75000)
    student = Student("Alice", 20, "alice@uni.edu", "S12345", "Data Science")
    staff = Staff("Bob", 35, "bob@uni.edu", "HR Manager")

    # Polymorphism: Treat all as Person objects
    people = [lecturer, student, staff]

    for person in people:
        print(f"\n{person}")
        print(f"Role: {person.role()}")
        
        # Check instance-specific methods
        if isinstance(person, Lecturer):
            print(person.teach("Algorithms"))
        elif isinstance(person, Student):
            print(person.study())
        elif isinstance(person, Staff):
            print(person.manage())