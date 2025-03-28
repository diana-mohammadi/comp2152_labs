class Person:
    def __init__(self, p_name, p_age, p_height):
        print("Constructing the person object")
        self.__name = p_name
        self.__age = p_age
        self.__height = p_height
        self.public_prop = "I'm Public"

    # Getter for name
    @property
    def name(self):
        return self.__name

    # Setter for name
    @name.setter
    def name(self, new_name):
        self.__name = new_name

    def __del__(self):
        print("The garbage collector is automatically destroying the person object")



person1 = Person("Mark", 20, 6)

# version 1
print("The name of the person is: " + str(person1.name))  # No need for str() due to concatenation with a string

person1.name = "Alfred"
print("The name of the person is: " + str(person1.name))

print("Public " + str(person1.public_prop))