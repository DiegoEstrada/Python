class Parent:        # define parent class
   def myMethod(self):
      print ('Calling parent method')

class Child(Parent): # define child class
   def myMethod(self):
      print ('Calling child method')

c = Child()          # instance of child
c.myMethod()         # child calls overridden method



class JustCounter:
    __secretCount = 0

    def __init__(self):
        print("Counter created")

    def __del__(self):
        print("Destructor called")

    def __str__(self):
        return "Just a counter"

    def count(self):
        self.__secretCount +=1
        print(self.__secretCount)

counter = JustCounter()
print(counter)
counter.count()
counter.count()
#print (counter.__secretCount)
JustCounter._counter__setCount = 5;
print(JustCounter._counter__setCount)



