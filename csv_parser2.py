#Gilbert Lee

import csv #we import csv (has to be lower case) is because of the comma and quote parsing delimiter. If we just use the tools built into python, it lets us skip thinking about the quotation mark thing
print "CSV Parser"
print "^^^^^^^^^^"

# /////// READ IN THE FILE I WANT //////////
csv_file_path = "../Employee Info.csv" #this is the same thing as doing csv_filepath = "../" and csv_filename = "Employee Info.csv"
csv_file = open(csv_file_path)
csv_reader = csv.reader(csv_file) #
csv_rows = [] # we are copying what we read into an array of lines rather than a single array of all the info in one object
for row in csv_reader: #what we are doing is for every row, we are printing and copying the original row and appending it to the new row object 
	print row
	csv_rows.append(row)  
output = csv_file.read()  #so what is the difference between read and reader?
csv_file.close() #this is important for clearing up memory
print output

# /////// ACCESS THE STRUCTURE OF THE FILE ///////
print "^^^^^^^^^^"
print csv_rows[9] #->>gives us the 9th row, unless there is a header row
print csv_rows[9][3] #->> gives us 27, which is the 4th object in the 9th row, unless there is a header row
print "^^^^^^^^^^"

# ////// MANIPULATE THAT FILE /////////

#creating a multi variate conditional which is easier in here than in excel (the more conditions your statement has, the easier it is in python or sql)
def isYuppie(row): # the condition statement is whether they are a yuppie, and we are looking at that within the rows
	age = int(row[3]) # where location of the age is located so that is where the computer looks at and evaluates
	return age >= 20 and age <= 29
	#if age >= 20 and age <= 29
	# 	return True
	# else:
	# 	return False #we can substitute the entire if statement with just (return age >= 20 and age <= 29) cuz thats a boolean which evaluates for true and false

print "^^^^^^^^^^"
print isTargetAgeDemo(csv_rows[9])
print csv_rows[9]
print "^^^^^^^^^^"

modified_csv_rows = [] #creating objects to store al the modified rows

#append column to header
header_row = csv_rows[0]
header_row.append('Within Target Age Group')
modified_csv_rows.append(header_row)

print "^^^^^^^^^^"
print modified_csv_rows[0]
print "^^^^^^^^^^"

#append yuppie status to each row
for row in csv_rows[1:]: #leaving part after 1: automatically goes to last row
	row.append(isTargetAgeDemo(row)) #it automatically sticks the true false judge to the end
	modified_csv_rows.append(row) 

print "^^^^^^^^^^"
print modified_csv_rows[9]
print modified_csv_rows[9][3]
print modified_csv_rows[9][5]
print "^^^^^^^^^^"

# /////// WRITE OUT A NEW FILE /////////

wrote= open("Copy of Employee.csv","w+") #name of file being created
csv_writer = csv.writer(wrote)
wrote.write(output) #using the content within the stored object
for row in modified_csv_rows:
	csv_writer.writerow(row)
wrote.seek(0) #tells the code to go back to the beginning to read because otherwise python will continue reading where it last left off writing
print wrote.read() #has to have .read() to tell you what has jut been read
wrote.close
