

# this class can be imported, or written directly in the file it is used
class Car:

    


    # constructor
    def __init__(self, make, model, year, color):

        self.make = make

        self.model = model

        self.year = year

        self.color = color




    # method
    def drive(self):

        print(f"this {self.year} {self.color} {self.make} {self.model} is driving")


    # method
    def stop(self):

        print(f"this {self.year} {self.color} {self.make} {self.model} is stopped")