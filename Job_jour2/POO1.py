class Person:
    def __init__(self,Name,Age):
        self.Name = Name
        self.Age = Age

    def myfonction(self):
        print('My name is '+ self.Name)
        
person1 = Person("john", 20)
print(person1.Name)
print(person1.Age)
person1.myfonction()