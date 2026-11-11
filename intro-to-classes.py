# classes are like combining features from a dictionary with function that can give the object interactivity
# what is a class? A class is a blueprint for an object(dict) that contains some data (attributes, fields, prop.)

# method is a function that is part of a class
# functions do not need a class to be called
# methods use dot notation (.) to be called

class Person:
    name = "Nate" 
    age = 41


# now we need to create an instance foor the class.

instance1 = Person()

# to access we use dot notation

print(instance1.name)
print(instance1.age)

# instances maintain their own state

instance2 = Person()

instance2.name = "Aly"
instance2.age = 22

print(instance2.name)
print(instance2.age)
