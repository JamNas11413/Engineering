# Dunder or magic methods in Python 
    # Python magic (dunder) methods are special methods with double underscores __ that enable operator overloading and custom object behavior.   
                   # Operator overloading in Python allows you to redefine how built-in operators (like +, -, *, ==, and <) behave when used with your custom objects. Python implements this behavior through special methods, commonly referred to as dunder methods (double underscore methods) or magic methods. When an operator is used on an object, Python automatically translates that operator into its corresponding dunder method call under the hood. For example, when you use the + operator on two objects, Python internally calls the __add__ method of the first object, passing the second object as an argument. By defining these dunder methods in your class, you can customize how operators work with instances of your class, allowing for more intuitive and flexible code.
                   # custom object behavior refers to the ability to define how objects of a class should behave in certain situations, such as when they are printed, compared, or used in arithmetic operations. By implementing specific dunder methods in your class, you can control how instances of that class respond to various operations and interactions, making your objects more versatile and easier to work with in different contexts.

    # The below code displays the magic methods inherited by int class.


print(dir(int))


# Output

# ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '_...


# Explanation: dir(int) lists all attributes and methods of the int class, including magic (dunder) methods like __add__, __str__, etc.

# You can list magic (dunder) methods for any Python object via the terminal by following these steps:

#     Open the terminal or command prompt and type python3 to enter the Python console.
#     Use the dir() function to list all methods, e.g.

#     >>> dir(int)

# Output
    # ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '_...



# Magic methods in Python
    # Below are the lists of Python magic methods and their uses.
        # 1. Initialization and Construction
            #  __new__: To get called in an object's instantiation.
            # __init__: To get called by the __new__ method.
            # __del__: It is the destructor.

        # 2. Numeric magic methods
            # __trunc__(self): Implements behavior for math.trunc()
            # __round__(self,n): Implements behavior for the built-in round()
            # __abs__(self): Implements behavior for the built-in abs()
            # __neg__(self): Implements behavior for negation
            # __pos__(self): Implements behavior for unary positive 

        # 3. Arithmetic operators
            # __add__(self, other): Implements behavior for the + operator (addition).
            # __sub__(self, other): Implements behavior for the - operator (subtraction).
            # __mul__(self, other): Implements behavior for the * operator (multiplication).
            # __truediv__(self, other): Implements behavior for the / operator (true division).
            # __mod__(self, other): Implements behavior for the % operator (modulus).

        # 4. String Magic Methods
            # __str__(self): Defines behavior for when str() is called on an instance of your class.
            # __repr__(self): To get called by built-int repr() method to return a machine readable representation of a type.
            # __hash__(self): It has to return an integer, and its result is used for quick key comparison in dictionaries.
            # __bool__(self): Returns True or False to determine the truth value of an object, used in conditions and bool() calls.
            # __dir__(self): This method to return a list of attributes of a class.

        # 5. Comparison magic methods
            # __eq__(self, other): Defines behavior for the equality operator, ==.
            # __ne__(self, other): Defines behavior for the inequality operator, !=.
            # __lt__(self, other): Defines behavior for the less-than operator, <.
            # __gt__(self, other): Defines behavior for the greater-than operator, >.
            # __ge__(self, other): Defines behavior for the greater-than-or-equal-to operator, >=.

    # Examples of Magic Methods
    # 1. __init__ Method

    # __init__ method is automatically called when a new instance of a class is created. It is used to initialize the object’s attributes, similar to constructors in languages like C++, Java, C#, or PHP.

class String:
    
    def __init__(self, string):
        self.string = string
        
if __name__ == '__main__':
    
    s1 = String('Hello')
    print(s1)


# Output

# <__main__.String object at 0x791ce72aa900>

# Explanation:

    # __init__(self, string): Constructor that initializes the object with a string.
    # s1= String('Hello'): Creates an instance of String with 'Hello'.
    # print(s1): Tries to print the object. 

# 2. __repr__ method

# __repr__ method defines the official string representation of an object, primarily used for debugging. By default, it shows the type and memory address of the object.

class String:
    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return 'Object: {}'.format(self.string)

if __name__ == '__main__':
    str1 = String('Hello')
    print(str1)


# Output
# Object: Hello

# Explanation:

#     __repr__(self): Returns the official string representation of the object; used when printing or debugging.
#     str1 = String('Hello'): Creates an instance of String with 'Hello'.

# 3. __add__ method

# __add__ method method defines how objects of a class are added together using the '+' operator. It allows operator overloading.

# Adding __add__ method to String class: 

class String:
    
    def __init__(self, string):
        self.string = string 
        
    def __repr__(self):
        return 'Object: {}'.format(self.string)
        
    def __add__(self, other):
        return self.string + other

if __name__ == '__main__':
    
    string1 = String('Hello')
    print(string1 +' Geeks')


# Output

# Hello Geeks

# Explanation:

#     __init__(self, string): Initializes the object with a string.
#     __repr__(self): Provides a readable string representation of the object for debugging.
#     __add__(self, other): Overloads the + operator to allow adding a string to the object’s string attribute.
#     string1 + ' Geeks' – Calls __add__, returning 'Hello Geeks'.