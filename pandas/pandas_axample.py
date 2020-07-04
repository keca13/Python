import pandas as pd
num = pd.read_csv('C:\Users\user\Desktop\example.csv')
print(num)
line = num['col']
print(line)
line.to_csv('example2.csv', index = False)
