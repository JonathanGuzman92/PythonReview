#! usr/bin/python

# if Statement example
yourAge = int(raw_input("How old are you: "))

# Spaces are very important in Python
# Note that the () are not required but can make things easier to read
if (yourAge > 0) and (yourAge < 120):
    if (yourAge == 24):
        print "Same as me"
    elif (yourAge > 35):
        print "older than me"
    else:
        print "Younger than me"
else:
    print "Don't lie about your age"
    
    
""" Python has no switch statements

 switch(variable_passed):
 {
 case '1':
 perform action
 break
 
 case '2':
 perform action
 break
 
 default
 }
"""

# Here is one way to implement a switch statement

if (yourAge == 1):
    print 'test1'
elif (yourAge ==2):
    print 'test2'
    

# Conditional Statement

x, y = 1, 0

a = 'y is less than x' if(y<x) else 'x is less than y'

print a

