
# notice how these two classes are almost identical. in fact, there is only one line of code that is different, other than the class definition at the top.
class Cat:

    def __init__(self, name, age):

        self.name = name
        self.age = age


    def speak(self):

        print('Meow\n')



class Dog:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    
    def speak(self):

        print('Bark\n')