#! /usr/bin/python


# variables are called attributes in objects
# functions are called methods in objects

# Objects are instances of the class
class Animal:
    __hungry = "Yes"   # The __ two dashes make these attributes private
    __name = "No Name"
    __owner = "No Owner"
        
    # The class is defined as self. self is reference to the object
    def __init__(self): # __del__ is a deconstructor, or Garbage collector
        pass
    
    # Encapsulation makes it hard for anyone to change items in the object.
    # The only way to change the values with the __ is via the accessors

    # access to objects that should be hidden 
    def set_owner(self, newOwner):
        self.__owner = newOwner
        return
    
    def get_name(self):
        return self.__name
    
    def set_name(self, newName):
        self.__name = newName
        return
    
    def get_owner(self):
        return self.__owner
    
    def noise(self):
        print('Rhoooof!')
        self.__hiddenMessage()
        return
    
    # Hidden methods can also be encapsulated and called via other methods in the same object
    def __hiddenMessage(self):
        print("Can't get to this method directly")
        return


def main():
    dog = Animal() # creating animal object. Class is blueprint for object
    dog.set_owner('Roberto')
    print dog.get_owner()
    
    dog.noise()

if __name__ == '__main__': main()