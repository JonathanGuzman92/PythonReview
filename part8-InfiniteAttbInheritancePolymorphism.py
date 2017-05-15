#! /usr/bin/python

# variables are called attributes in objects
# functions are called methods in objects

# metclass allows you to use new python 3.0 objects in python 2.7
__metaclass__ = type


# Objects are instances of the class
class Animal:

    __name = "No Name"
    __owner = "No Owner"
        
    # Allow for infinite number of attributes **kvargs Dictionary full of tuples
    # "Real" constructor setup
    def __init__(self, **kvargs): 
        self._attributes = kvargs

    def set_attributes(self, key, value):
        self._attributes[key] = value
        return
    
    def get_attributes(self, key):
        return self._attributes.get(key, None)
    
    def noise(self):
        print('Rhoooof!')
        return
    
    def move(self):
        print('The animal moves forward')
        return
    
    def eat(self):
        print('Munch, Munch')
        return


# INHERITANCE - get all the attributes and methods of animal 

class Dog(Animal):
    
    # constructor for new class - Call main constructor above
    def __init__(self, **kvargs):
        super(Dog, self).__init__() # not usable in python 2.7 without including __metaclass__ = type
        self._attributes = kvargs
    
    # Method overriding. The java interpreteur automatically knows to override the methods
    # contained in the Animal class
    def noise(self):
        print('Woof')
        Animal.noise(self)
        return

class Cat(Animal):
    
    def __init__(self, **kvargs):
        super(Cat, self).__init__() # not usable in python 2.7 without including __metaclass__ = type
        self._attributes = kvargs
        
    def noise(self):
        print('Meow')
        Animal.noise(self)
        return
    
    def noise2(self):
        print('Purrr')
        return

# new class of type Dog and Cat
# Which ever class is called first defines the class methods below first
class Dat(Dog, Cat):
    def __init__(self, **kvargs):
        super(Dat, self).__init__()
        self._attributes = kvargs
    def move(self):
        print('Chases Tails')
        return
    
# POLYMORPHISM - Any object inherited from animal will be accepted
# When individual methods are called, original method is called
def playWithAnimal(Animal):
    Animal.noise()
    Animal.eat()
    Animal.move()
    print(Animal.get_attributes('__name'))
    print(Animal.get_attributes('__owner'))
    print('\n')
    Animal.set_attributes('clean', 'Yes')
    print(Animal.get_attributes('clean'))

def main():
    bob = Dog(__name='bob', __owner='Raul')
    isabel = Cat(__name='isabel', __owner='Rob')
    
    #POLYMORPHISM - pass object of type Animal
    playWithAnimal(bob)
    playWithAnimal(isabel)
    
    japh = Dat(__name= 'japh', __owner = 'Reloo')
    japh.move()
    japh.noise()
    japh.noise2()
    print japh.get_attributes('__name')
    
    print issubclass(Cat, Animal)
    print Cat.__bases__
    print isabel.__class__
    print isabel.__dict__


if __name__ == '__main__': main()