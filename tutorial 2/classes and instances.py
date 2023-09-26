

# a class is like a blueprint for creating instances. and each employee created with the 'Employee' class will be an instance of that class.
class Employee:

    # instance variables contain data that is unique to each instance.
    def __init__(self, first, last, pay):

        self.first = first
        self.last = last
        self.email = f"{first}.{last}@company.com"
        self.pay = pay


    
    def fullname(self):

        return "{} {}\n".format(self.first, self.last)

    pass


emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "User", 60000)


# instance variables can be created manually like this
# this sucks tho
    # emp_1.first = 'Corey'
    # emp_1.last = 'Schafer'
    # emp_1.email = f"{emp_1.first}.{emp_1.last}@company.com"
    # emp_1.pay = 50000

    # emp_2.first = 'Test'
    # emp_2.last = 'User'
    # emp_2.email = f"{emp_2.first}.{emp_2.last}@company.com"
    # emp_2.pay = 60000

# print(emp_1)
# print(emp_2)

# print(emp_1.email)
# print(emp_2.email)

print(emp_1.fullname())
print(emp_2.fullname())

print(Employee.fullname(emp_1))
print(Employee.fullname(emp_2))