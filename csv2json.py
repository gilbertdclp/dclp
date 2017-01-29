#Gilbert Lee

import csv #step 1 of converting a csv file into json


# /////// READ IN THE FILE I WANT //////////
csv_file_path = "../Employee Info.csv" #this is the same thing as doing csv_filepath = "../" and csv_filename = "Employee Info.csv"
csv_file = open(csv_file_path)
csv_reader = csv.reader(csv_file) #
csv_rows = [] # we are copying what we read into an array of lines rather than a single array of all the info in one object
for row in csv_reader: #what we are doing is for every row, we are printing and copying the original row and appending it to the new row object 
	print row
	csv_rows.append(row)  
csv_file.close() #this is important for clearing up memory

header_row =csv_rows[0]
value_rows = csv_rows[1:]


# /////// WRITE OUT A NEW FILE /////////

for index, column_name in enumerate(header_row):
	header_row[index] = column_name().replace(" ", "-")

#=================================part 2 to convert to json

import json
from pprint import pprint


#read in the file i WANT

data = json.load(csv_file)
pprint(data) #previewing the data


# WRITE OUT THE DATA I WANT

outfile = open("Jsonresult.json","w+")  #name of file being created
json.dump(data, outfile, sort_keys=True, indent=4, separators=(',', ': '))

