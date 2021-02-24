import random
import re
from collections import Counter
import shutil
import os
import datetime
import math
import numpy
import timeit
import time
import zipfile

# print(os.getcwd())
#
# myTime = datetime.datetime.today()
# print(myTime)
#
# help(numpy)

# random.seed(101)
# print(random.randint(0,100))
# print(random.randint(0,100))
# print(random.randint(0,100))
# print(random.randint(0,100))
# print(random.randint(0,100))
#
# pattern = r'[^\d]+'
# phrase = 'there are 3 numbers 34 inside 5 this sentence'
# print(re.findall(pattern, phrase))

stmt = '''
func_one(100)
'''
setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''
print(timeit.timeit(stmt, setup, number=1000))
