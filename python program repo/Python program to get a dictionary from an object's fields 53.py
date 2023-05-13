class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

person = Person("John", 25, "New York")

person_dict = person.__dict__
print("Dictionary from object's fields:", person_dict)
