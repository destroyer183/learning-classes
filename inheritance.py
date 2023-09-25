# this is a cleaned up version of the inheritance example, which does not use inheritance.


# this class contains the functionality that the 'Cat' and 'Dog' classes use.
# calling this class 'Pet' is a generalization, whereas 'Cat' and 'Dog' are more specific.
# any class that inherits from this class are called 'child' classes or 'derived' classes.
class Pet:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    
    def show(self):

        print(f"I am {self.name}, and {self.age} years old.\n")


    
    def speak(self):

        print('I dont know what I say\n')



# the classes 'Cat' and 'Dog' inherit the functionality of an upper-level class by putting the upper-level class in brackets.
# 
class Cat(Pet):

    def __init__(self, name, age, color):

        # 'super' references the parent class, '__init__' defines the method we want to call, and 'name' and 'age' are the arguments passed.
        super().__init__(name, age)

        self.color = color



    def show(self):

        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}.\n")



    def speak(self):

        print('Meow\n')


class Dog(Pet):

    def speak(self):

        print('Bark\n')



class Fish(Pet):

    def identify(self):

        print(f"I am {self.name}\n")

    pass




p = Pet('Tim', 19)

p.show()
p.speak()

c = Cat('Bill', 34, 'Brown')

# even the function 'show()' is not defined in the 'Cat' class, it still works because it 'inherits' the properties from the 'Pet' class.
c.show()
# even though the 'speak()' method is defined in the 'Pet' class and the 'Cat' class, 
# if there is a method defined in a lower-level class with the same object type as the variable it was called on, 
# it will automatically override the upper-level class, because the lower-level class is more specific to that class.
c.speak()

d = Dog('Jill', 25)

d.show()
d.speak()

f = Fish('bubbles', 10)

f.identify()
# because there is no method called 'speak()' in the 'Fish' class, it will automatically use the one in the upper-level class.
f.speak()