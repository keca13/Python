#simply2.py
# #!/usr/bin/env python3
# http://zetcode.com/python/jinja/

from jinja2 import Template

name = "jack"
age = 40

tm = Template("My name is {{name}} and I am {{age}}")

msg = tm.render(name=name, age=age)

print(msg)
