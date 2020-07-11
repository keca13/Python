import sys


def fun_test():
	# plik wyjsciowy
	file = sys.argv[1]
	# plik wychodzacy
	file_out = sys.argv[2]
	with open(file) as f, open(file_out, 'w') as out:
		while i := f.readline():
			i * 2
			out.write(i.lstrip())



fun_test()
