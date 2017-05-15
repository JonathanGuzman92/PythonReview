# !usr/bin/python

# Dictionary

# List and Tuples use index
# Dictionaries use keystroke

dictionaryEx = ({"Age":24,"Height":"6'0","Weight":190})

# Dictionaries are immutable, can't change values, only overwrite is ALLOWED_KEYS

print dictionaryEx

print dictionaryEx.get("Height")  # Get item based on key

print dictionaryEx.items()  # print the items in the dictionary

print dictionaryEx.values()  # print the values in the dictionary 

dictionaryEx.pop("Height")  # delete the height item

print dictionaryEx


# Printing functions in python

strName = 'Jon'
floatAge = 24
charSex = 'M'
intKids = 0
boolMarried = False

# The comma will automatically place the spac
print 'My Name is' + strName

# The % are used to fill in the missing items
# the %.1f will round to one decimal 
print '%s is %.1f years old' % (strName, floatAge)
print 'Sex: %c' % (charSex)
print 'He has %i kids and said it\'s %s he is married' % (intKids, boolMarried)

import math
print '%.15f' % (math.pi) # print pi to 15 points of accuracy 
print '%20.15f' % (math.pi) # print 15 decimal points with 20 spaces to the left
print '%-25.15f is the value of pi' % (math.pi) # print 15 decimal points with 25 spaces to the right

precisionPi = int(raw_input("How precise should pi be: "))
print 'Pi = %.*f' % (precisionPi, math.pi) # The * represents the precision 
 
 
bigString = 'Here is a long string that I will be messing with'
 
print bigString[1:20:2] # print from first element to 20th every other character
 
print bigString.find('string') # find the element where the string is located 

print bigString.count('e') # count the chars

print bigString.count('e', 4, 20) # count the number of e's from 4th element up to 20th
 
print bigString.upper()

print bigString.lower()

print bigString.replace('long', 'small')
 
# turn the string into a tuple 
copyString = tuple(bigString)
print copyString

# turn tuple back into String
print ''.join(copyString)

# join tuple with ', ' character
print ', '.join(copyString)

# split your string dependent on where the spaces are located
print bigString.split(' ')

# strip() function removes all white spaces
randomWhite = '     Random White Spaces     '
print randomWhite.strip()



