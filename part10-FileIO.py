#! usr/bin/python

# module to interact with file management system
import os
from __builtin__ import file

def retrieveFile():
	try:
		# create a dictionary of students
		bestStudent = {}
		bestStudentStr = "The Best Students Ranked\n\n"
		# create a file reader
		f = open('studentgrades.txt')
		
	except(IOError), e:
		print "File not found", e
	else:
		# read each line in file
		for line in f:
			name, grade = line.split()
			bestStudent[grade] = name
		f.close()
		
		for i in sorted(bestStudent.keys(), reverse=True):
			print (bestStudent[i] + ' scored a ' + i)
			bestStudentStr += bestStudent[i] + ' scored a ' + i + "\n"
		print "\n"
		
		print bestStudentStr
		
		outToFile = open("studentrank.txt", "w")
		outToFile.write(bestStudentStr)
		outToFile.close()
		
		print "Finished Output"
	return

def directoryPlay():
	print os.listdir("/usr")
	print os.path.isdir("/usr/bin/python")
	print os.path.isfile("/usr/bin/python")
	
	dirList = os.listdir("/usr")
	
	for file in dirList:
		if os.path.isdir("/usr/" + file):
			print os.listdir("/usr/" + file)
		else:
			continue
	return

	# You can make and remove directories easily with the os library 
	#os.mkdir("/Users/jon/Documents/Test")
	#os.rmdir("/Users/jon/Documents/Test")
	
	
def main():
	retrieveFile()
	directoryPlay()
	
	
if __name__ == '__main__': main()