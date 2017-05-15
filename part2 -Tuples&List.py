#! /usr/bin/python

# Tuples, List, and Dictionaries are like arrays

# Tuples are immutable (Each Element cannot be changed one at a time)
# List can are mutable (Individual Elements can be changed)
# Dictionaries have Keys and Values

# TUPLES

tupleExample1 = ('Jon', 25, 'Seattle', 'WA')

print tupleExample1 # print the tuple
print tupleExample1[2] # print Seattle

tupleExample2 = tuple('abcd') # turn a string into a tuple

print tupleExample2 # prints the new tuple ('a', 'b', 'c', 'd')
print tupleExample2[0:2] # prints ('a', 'b')


# LIST

listExample1 = ['Jon', 25, 'Seattle', 'WA']

print (listExample1)
print listExample1[0:2]
print listExample1[-1] # print the last value

listNumbers = [1,2,3,4,5,6,7,8,9,10]

print listNumbers[-3:] # print the last three numbers
print listNumbers[:3] # print the first three numbers
print listNumbers[1:10:2] # print every other digit starting at 1

print len(listNumbers) # print the length of the list

print min(listNumbers) # print the maximum value in the list
print max(listNumbers) # print the minimum value in the list

listName = list('Name') # turn the string into a List
print listName # print the list

listName[4:] = 'ADD' # add the new letters 'A' 'D' 'D' to list
print listName
print ''.join(listName) # print out the item as a string

listExample2 = [1,2,3,4]
listExample2[1] = 5  # change element 2 to a 5
print listExample2

del listExample2[1] # delete element 2
print listExample2

listExample1.append('AppendItem') #add onto end of list
print listExample1

listExample1.remove('AppendItem') # remove based on item name
listExample1.remove(listExample1[3]) # remove based on index
print listExample1

listExample1.insert(2, 'WA') # add item to second spot
print listExample1

listExample2 = ['d','g','r','s','h','q','a']
listExample2.sort() # sort the list

print listExample2


listExample3 = [ ['a', 'b', 'c'], ['c','d','e'], ['f','g','h'] ] # multidimensional

print listExample3[2][1] #select third list group and second item




