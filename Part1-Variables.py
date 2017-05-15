#! /usr/bin/python

# Comment

# all you need to import a library

import math

integerEX = 8

longIntEx = 200000000000000L

floatEx = 2.2

stringEx = "Hello"

booleanEx = True

print type(integerEX)
print type(longIntEx)
print type(floatEx)
print type(stringEx)
print type(booleanEx)


booleanTwo = False

print booleanEx and booleanTwo
print booleanEx or booleanTwo
print not booleanEx

intOne = 7
intTwo = 99
floatOne = 7.9
floatTwo = 9.8

print intTwo / intOne 
print float(intTwo) / float(intOne)
print int(floatOne)

print int(booleanEx)


print math.sqrt(intOne)

answer = raw_input("What is your name?")
print "Hello", answer

longStr = '''This is a very long string of text \
that goes on and on '''

longStr2 = 'How are you "Hi doing" '

# \n  new line ,  \' include a black slash character, " " ' ', ''' ''' multiple line quote 

print longStr
