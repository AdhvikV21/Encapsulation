# Class creation
class MyClass:

        # private variable
        __privateVar = 27

        # private method
        def __privMeth(self):
                print("I'm inside class myClass")

        # Function to print value of private variable
        def hello(self):
                print("Private Variable value: ",MyClass.__privateVar)

# Object creation and method call
foo = MyClass()
foo.hello()
foo.__privMeth