# Modules

import useful_tools  # ???
# Why am I not able to create my own module useful_tools?

import json
print(json.decoder)

# PIP is a package manager

# Classes & Objects
# See Student.py for the Class student

from Student import Student

# An object is an instance of a class
student1 = Student(
    "Isaac",
    "Computer Science",
    4.2,
    False
)

student2 = Student(
    "Benjamin",
    "Underwater Basket Weaving",
    2.0,
    True
)

print(student1.name)
