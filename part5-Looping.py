#! usr/bin/python

listExample = [4,5,6]

stringExample = "Random String"

# in operator
# in operator searches for value in string or list

print 3 in listExample
print "String" in stringExample


# WHILE statement
x = 1

while (x <= 30):
    print x,  # The comma allows you to print everything on one line 
    x += 1

print ''

# FOR Statement

listNum = [0,1,2]
listName = ['Rob Smith', 'Will Smith', 'Rocky Balboa']
listAge = [23,26,22]

for i in listNum:
    print '%s is %d' % (listName[i], listAge[i])


listExample = [1,2,3,4]

for i in listExample:
    print i,
    
for i in range(1,31):
    print i,

listExample2 = range(1,31)

for i in listExample2:
    if (i%2) == 0: # check if value is divisible by 2
        continue # jump out of current iteration
    elif i == 25:
        break # break out of loop all together
    else:
        print i,


