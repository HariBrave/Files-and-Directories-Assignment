# Function that creates a file in the directory of your choosing

import os

def main():

	directory = input("Enter the directory that you want to save the file: ")
	
	filename = input("Enter the file name: ")
	
	name = input("Enter your name: ")
	
	address = input("Enter your address: ")
	
	phone_number = input("Enter your phone number: ")

	# Checking if the directory exists
	
	if os.path.isdir(directory):
	
		# Creating and opening the file to Write
		
		writeFile = open(os.path.join(directory,filename),'w')
		
		# Writing the data
		
		writeFile.write("Name: "+name+'\n''Address: '+address+'\n''Phone Number: '+phone_number+'\n')
		
		# Close the file after writing is done
		
		writeFile.close()

		print("File Contents")
		
		# Reading the file inside the program to ensure creation
		
		readFile = open(os.path.join(directory,filename),'r')
		
		for line in readFile:
			print(line)
		
		readFile.close()
		input("Press ENTER to exit...")
	else:
		print("Sorry that directory does not exist...")
		input("Press ENTER to exit...")

main()
