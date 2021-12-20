import random

class Animal:
    def talk(self):
        print("Hello")

class Dog(Animal):
    def talk(self):
        print("woof woof")
        
class Cat(Animal):
    def talk(self):
        print("meow")
        
c = Cat()
c.talk()
d = Dog()
d.talk()
a = Animal()
a.talk()

