python


>>> with open('dokument.crt') as input, open('zapis_dokumenty.crt', 'w') as output:\
... non_blank = (line for line in input if line.strip());\
... output.writelines(non_blank)
...
>>>
