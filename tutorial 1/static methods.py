# static methods are useful when you have a large amount of functions and you want to organize them into one class.

class Math:

    # these methods do not have access to any instances of the class they are in, just like class methods.
    # they do something, but they don't change anything.
    @staticmethod
    def add5(x):

        return x + 5
    

    @staticmethod
    def add10(x):

        return x + 10
    

    @staticmethod
    def pr():

        print('run')



print(Math.add5(5))
print('')
Math.pr()