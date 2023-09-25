
class Person:

    # this is a class attribute. this is because it does not use 'self'.
    # because it isn't defined inside of any method, and because it does not have access to an instance of the class, it is defined for the entire class.
    # this means that this is not specific to any instance, and it won't change for each instance of the 'Person' class.
    number_of_people = 0

    def __init__(self, name):

        self.name = name

        Person.add_person()


    # this is a clas method. this method will not be acting on behalf of one instance. it will not be specific to one instance.
    # while it can be called on an instance, it will not be very useful or effective.
    # this is meant to be called on the class itself, so that it can deal with something like returning the number of people that are associated with this class.
    # this is a class method, which means they act on the class itself, 
        # they do not have access to any instance, which is why 'cls' is written where 'self' is usually written, 
        # because there it is not supposedto be acting on any object, because it is just acting on the class 'Person'.
    @classmethod
    def num_of_people(cls):

        return cls.number_of_people()
    

    @classmethod
    def add_person(cls):

        cls.number_of_people += 1

    

p1 = Person('tim')
p2 = Person('jill')

print(f"number of people: {p1.number_of_people}\n")

# this works because the class attribute is specific to the class 'Person', not an instance of the class 'Person'.
# this means that it can be changed using the name of the class.
print(f"number of people: {Person.number_of_people}\n")

Person.number_of_people = 8

# because p1 doesn't have an attribute called 'number_of_people', 
    # python instead looks to see if the class has an attribute called 'number_of_people' 
    # and if an attribute called 'number_of_people' is found, it will display that instead.
print(f"number of people: {p1.number_of_people}\n")

Person.number_of_people = 9

print(f"number of people: {p2.number_of_people}\n")

print(Person.number_of_people)