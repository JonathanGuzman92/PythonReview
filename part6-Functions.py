#! /usr/bin/python

# The default values are 1 and 1
def addNumbers(numOne=1, numTwo=1):
    return numOne + numTwo

globalVariable = 10 # This variable is global, i.e. functions outside can access it

# How to pass unlimited values into function (NOTE* the function overload)
def addNumbers(*args):
    finalValue = 0 # This is a local variable, i.e. it can only be accessed within the
                   # function where it is created
    
    globalVariable = 15 # Global variables can only be temp changed inside a method
    
    print type(args)
    
    # check if args has any values
    if args:
        for i in args:
            finalValue += i
        return finalValue
    else:
        return "Please provide numbers"

# How to change global variables
def changeGlobal():
    # First way is to change the variable as global
    global globalVariable
    globalVariable = 15
    
    # Second way is to convert it as you change the variable
    globals()['globalVariable'] = 20
    
# pass unlimited numbers of keys (for dictionary use)
# create a dictionary full of tuples
def createDict(**kvargs):
    for i in kvargs:
        print i, kvargs[i]
    print type(kvargs) #kvargs is a dictionary <type 'dict'>
    return
    

# Recursion example with factorials
# 4! = 4*3*2*1
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)
    
    
    
"""  This is what occurs with recursion. Every time the function is called
     you are essentially calling a new instance of the method

def factorial(3):
    if 3 == 1:
        return 1
    else:
        return 3 * factorial(3-1)

def factorial(2):
    if 2 == 1:
        return 1
    else:
        return 2 * factorial(2-1)
        
def factorial(1):
    if 1 == 1:
        return 1
    else:
        return 1 * factorial(1-1)

"""

# function called main
def main():
    #pass
    #use pass to not trigger errors when initially defining code
    
    print addNumbers()
    print addNumbers(50,60)
    print addNumbers(50,20,29,103)
    print globalVariable
    changeGlobal()
    print globalVariable
    
    # create a single tuple
    createDict(Name='Jon', Age=24, YearBorn=1992)
    
    # create a dictionary with multiple tuples
    createDict(Cust1=('Jon', 24, 1992),Cust2=('Alb', 37, 1980),Cust3=('Bet', 37, 1980))
    
    print factorial(4) 
# used to define what function to call when program called
# Tells java interpreter to call main
if __name__ == '__main__': main()