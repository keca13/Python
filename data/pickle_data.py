#https://www.journaldev.com/15638/python-pickle-example
import pickle

## Part 01 from input to  list
number_of_date = int(input('Podaj liczbe hasel: '))

data = []


for i in range(number_of_date):
	raw = input('Haslo '+ str(i)+' : ')
	data.append(raw)

print("list before writed",data)

##Part 02 write list to binary file


file = open('important', 'wb')

pickle.dump(data, file)

file.close()


## Part 03 open a file, where you stored the pickled data
file = open('important', 'rb')

# dump information to that file
data = pickle.load(file)

# close the file
file.close()

print('Showing the pickled data:')

cnt = 1
for item in data:
    print('haslo :  ', cnt, ' is : ', item)
    cnt += 1
