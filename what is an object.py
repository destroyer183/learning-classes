

# x is equal to the object that is a type "int" with the value "1"
x = 1
y = 'hello'

# notice how it prints <CLASS 'str'> this means that the inputted string is actually an object of the class "str"
print(type('hello'))

# same thing here
print(type(x))

# and same thing here as well. the function hello() is an object with a class called 'function'
def hello():

    print('hello')

print(type(hello))

# because these are different object classes, they can't be added together.
# in other words, the addition operation is not defined for objects of 'int' and objects of 'str' being added together
try:
    print(x + y)
except:pass

print('\n\n\n')