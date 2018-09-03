class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
               # unexpectedly shared by all dogs

print(d.name +" is able to do :")
print(d.tricks)
print(e.name +" is able to do :")
print(e.tricks)
div = "#"
print(div*50)

class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')

print(d.name +" is able to do :")
print(d.tricks)
print(e.name +" is able to do :")
print(e.tricks)
