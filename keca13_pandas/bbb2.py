#!  python3
import csv


new_row = input("Write date to 'bbb.csv' file: >>>")

def openfile():
	with open('bbb.csv', 'a', newline='',) as csvfile:
		employee_writer = csv.writer(csvfile, delimiter=' ', escapechar=' ', quoting=csv.QUOTE_NONE)
	#employee_writer.writerow(['name', 'department', 'started', 'lllllll'])
		employee_writer.writerow([new_row,])
	#employee_writer.writerow(['Erica Meyers', 'IT', 'March'])

#openfile()
