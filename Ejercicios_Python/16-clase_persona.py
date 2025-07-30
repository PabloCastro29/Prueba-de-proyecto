class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def mayor(self):
        return self.age >= 18
Persona1 = Person("Diana", 20) 
print(Persona1.name, "Es mayor de edad?", Persona1.mayor())