# Lesson 6-76 importする際の記述の仕方
import collerctions
import os
import sys

import termcolor

import lesson_package

import config

print(collerctions.__file__)
print(termcolor.__file__)
print(lesson_package.__file__)
print(config.__file__)

print(sys.path)
