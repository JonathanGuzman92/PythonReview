#! usr/bin/python

import shelve #Library that emulates a database


def addCustomer(database):
	customer = {}
	
	print "Add a new customer to the database\n"
	
	custNum = raw_input('Enter a customer number: ')
	customer['fistName'] = raw_input('Customer First Name: ')
	customer['lastName'] = raw_input('Customer Last Name: ')
	customer['streetAdd'] = raw_input('Customer Street Address: ')
	customer['city'] = raw_input('Customer City: ')
	customer['state'] = raw_input('Customer State: ')
	customer['zip'] = raw_input('Customer Zip Code: ')
	
	database[custNum] = customer
	return
	
	
def main():
	database = shelve.open('customers.dat', writeback=True)

	addCustomer(database)
	
	lookForCustomer = 1
	
	while(lookForCustomer != '0'):
		lookForCustomer = raw_input("Enter Customer Number(0 to Exit)")
		
		if lookForCustomer == '0':
			break
		else:
			try:
				for i in database[lookForCustomer]:
					print i, " ", database[lookForCustomer][i]
			except KeyError:
				print "Customer not in database"
				break
			else:
				print "\n"
				
	database.close()
				
if __name__ == '__main__': main()