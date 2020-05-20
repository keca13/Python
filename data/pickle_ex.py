#! python3

# pickle_ex.py
#http://zetcode.com/lang/python/files/

import pickle


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


person = Person('Monica', 15)
print(person.get_name())
print(person.get_age())

with open('monica', 'wb') as f:
    pickle.dump(person, f)

with open('monica', 'rb') as f2:
    monica = pickle.load(f2)

print(monica.get_name())
print(monica.get_age())
