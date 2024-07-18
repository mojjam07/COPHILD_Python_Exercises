# class of 30/5/2024 by Mr. Teejay

#-1-PYTHON MODULE
  #-a-pypi.org :: print(dir(module))
  #-b-pre-packaged
  #-c-user defined

#-2-PYTHON DATES
#-3-PYTHON MATHS
#-4-PYTHON JSON
  #-a-object literal
  #-b-new keyword
  #-c-object constructor

#-5-PYTHON REGEX

import mod, platform
import datetime
import math
import json
import re

print(dir(mod))
print(dir(platform))
print(platform.system())
print(platform.processor())
print(platform.version())

print(dir(datetime))
today = datetime.datetime.now()
print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.strftime('%B'+'/'+'%d'+'/'+'%Y'))

mod.myFunc(7, 5)
mod.myFunc(8, 5)

print(mod.x)
print(type(mod.x))
print(type(mod.myFunc))

print(dir(math))
x = math.floor(256)
y = math.pow(5, 3)
p = math.pi
f = math.factorial(6)
print(x)
print(y)
print(p)
print(f)

print(dir(json))
x = '{"name": "mojjam", "age": 32}'
p = json.loads(x) # : load - Convert JSON => python
print(type(p))
print(p)

y = {"name": "mojjam", "age": 32}
p = json.dumps(y) # : dumps - Convert python => JSON
print(type(p))
print(p)

print(dir(re))