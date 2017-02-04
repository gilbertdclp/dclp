#Gilbert Lee

import csv

# reading file
csv_filename = "ACH_Data_mon_1.csv"
csv_file = open(csv_filename)
csv_reader = csv.reader(csv_file)
csv_rows = []
for row in csv_reader:
	# print row
	csv_rows.append(row)
csv_contents = csv_file.read()
# csv_file.close()

# print csv_rows

# writing files for each column
# print csv_rows[0]
index = 1
csv_filename_new = csv_rows[index][1] + ' ACH_Transactions_mon_1.csv'
csv_file_new = open(csv_filename_new, "w+")
csv_writer = csv.writer(csv_file_new)
csv_writer.writerow(csv_rows[0])
csv_writer.writerow(csv_rows[index])
for row in csv_rows[2:]:
	# print row[1]
	if row[1] == csv_rows[index][1]:
		csv_writer.writerow(row)
	else:
		csv_filename_new = row[1] + ' ACH_Transactions_mon_1.csv'
		csv_file_new = open(csv_filename_new, "w+")
		csv_writer = csv.writer(csv_file_new)
		csv_writer.writerow(csv_rows[0])
		csv_writer.writerow(row)
	index += 1
csv_file_new.close()
