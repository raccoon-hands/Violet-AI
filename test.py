from dictionaries import *
import re

a_dict = networking
new_dict = {}

for key in a_dict:
    newkey = re.sub('[^A-Za-z0-9]+', '', key).lower()
    new_dict[newkey] = a_dict[key]

print(new_dict)

