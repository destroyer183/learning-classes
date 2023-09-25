

class Dog:

    # this is a special method. whenever a new dog instance is created (line 23), init will be called, 
    # and any arguments located inside it will be passed to the init method.
    def __init__(self, input, num, age):

        print(f"self: {self}\n")

        # this is an 'attribute' of the class 'Dog' which is 'name', that is equal to the argument 'input'
        # every time a new 'Dog' object is created, you will pass a name with the 'name' parameter.

        # the point of this attribute is that it is stored permanently, for each specific object.
        self.name = input

        self.number = num

        self.age = age

        print(input)
        print(self.name)

        print('')

        pass


    def get_name(self):

        return f"name of dog {self.number}: {self.name}\n"
    


    def get_age(self):

        return f"age of dog {self.number}: {self.age}\n"
    


    def set_age(self, age):

        self.age = age



    def add_one(self, x):

        return x + 1



    def bark(self):

        print('bark')



# while this works, what if you want 25k dogs? or every time the code runs, a different amount of dogs are made? you can't!
dog1_name = 'Tim'

dog1_age = 34

# but what about this?
# well this works, but it is very annoying to find the correct index and access it.
dogs_name = ['Tim', 'Bill']

dogs_age = [32, 14]




# there are two different 'Dog' objects
d = Dog('Tim', 0, 34)

d2 = Dog('Bill', 1, 12)
# even though the init method was not called, because a new 'Dog' object was created, it automatically passed the input to the name parameter, and then printed it out.

print(f"dog {d.number} name: {d.name}\n")

print(f"dog {d.number} name: {d2.name}\n")


print(d.get_name())

print(d2.get_name())


print(d.get_age())

print(d2.get_age())


d.set_age(23)

d2.set_age(11)

print(d.get_age())

print(d2.get_age())


# prints <class '__main__.Dog'>
# the underscores represent which module the class was defined in
print(type(d))

print('')

# calls the method 'bark' on the object with type 'Dog' 
d.bark()

print('')

# when the method 'add_one' is called, you need to pass in a value(s) to represent the variables needed.
print(d.add_one(5))

print('')