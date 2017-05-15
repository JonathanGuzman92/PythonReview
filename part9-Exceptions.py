#! /usr/bin/python

import exceptions


class Dog:
	__secrete = 33

def main():
	# These are all of exceptions in the python library
	#for i in dir(exceptions):
	#	print i
	
	# Create your own exception
	# raise Exception('Just Disagree')
	
	# This will raise an attribute exception because of the secrete attribute 
	# doogy = Dog()
	# print doogy.__secrete
	
	# This will raise an IOError - i.e. the file does not exist
	#f = open('student.txt')
	
	# This will raise an IndexError
	# listEx = [1,2,3]
	# print listEx[4]
	
	# This will raise a KeyError - Name does not exist
	# dictEx = ({'Age':35})
	# print dictEx['Name']
	
	# This will raise a NameError - monkey does not exist
	# print monkey
	
	# TypeError
	# print 'Tomato' % 5
	
	# cannot divide by zero error
	try:
		zeroDivision = 1/0
	except ZeroDivisionError:
		print "You can't divide by zero"
	
	# show multiple errors
	try:
		zeroDivision = notHere/0
	except (NameError,ZeroDivisionError), e:
		print "You can't divide by zero"
		print e
	
	# What happens when there is no error
	try:
		zeroDivision = 1.0/2.0
	except (NameError,ZeroDivisionError), e:
		print "You can't divide by zero"
		print e
	else:
		print zeroDivision
	finally:
		print 'This will always occur'
	
	
	
if __name__ == '__main__': main()