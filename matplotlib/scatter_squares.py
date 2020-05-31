import matplotlib.pyplot as plt 
#x_values = [1,2,3,4,5]
x_values = range(1,10)
#y_values = [1, 4, 9, 16, 25]
y_values = [x**2 for x in x_values]
plt.style.use('seaborn-ticks')

fig, ax = plt.subplots()

#ax.scatter(2, 4, s=200)
ax.scatter(x_values, y_values,c = 'red', s=10)
ax.plot(x_values, y_values, linewidth=6)

#Zdefiniowanie tytułu wykresu i etykiet osi
ax.set_title("Kwadrat liczb", fontsize=24)
ax.set_xlabel("Wartość", fontsize=14)
ax.set_ylabel("Kwwadraty wartości", fontsize=14)

#Zdefiniowanie wielkości etykiet
ax.tick_params(axis='both', which='major', labelsize=14)

#Zdefiniowanie zakresu dla każdej osi
#ax.axis([0, 1100, 0, 1100000])

plt.show()