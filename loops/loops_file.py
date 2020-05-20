tab = []
for line in open("mtcars.csv", "r"):
	tab.append(line)
print(tab)

tab.append("zlowo")
tab.extend("zlowo2")

with open("mtcars2.csv", "w") as output:
	output.writelines(tab)

print(tab)
