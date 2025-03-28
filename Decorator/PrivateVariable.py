class MyClass:
    def __init__(self, value):
        self.__private_var = value  # Private variable

    @property
    def value(self):
        """Getter method to retrieve the private variable"""
        return self.__private_var

    @value.setter
    def value(self, new_value):
        """Setter method to update the private variable"""
        self.__private_var = new_value


# Example usage
obj = MyClass(10)
print("Initial Value:", obj.value)  # Access using property (getter)

obj.value = 20  # Modify using property (setter)
print("Updated Value:", obj.value)  # Access updated value