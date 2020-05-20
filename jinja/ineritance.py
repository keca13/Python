#ineritance.py
#!/usr/bin/env python3

from jinja2 import Environment, FileSystemLoader

content = 'This is about pagekkkkk'

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

template = env.get_template('about.html')

output = template.render(content=content)
print(output)