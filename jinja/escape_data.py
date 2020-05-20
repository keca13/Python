#escape_data.py
#!/usr/bin/env python3

from jinja2 import Template, escape

data = '<a>Today is a sunny day</a>'

tm = Template("hey: {{ data | e}}")

msg = tm.render(data=data)

print(msg)
print(escape(data))