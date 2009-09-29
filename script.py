#!/usr/bin/python
from subprocess import *
from pylab import *

import re

p1 = Popen(["gnucap -b script.ckt"], shell=True, stdout=PIPE)
#input = p1.stdout.read()
result = []
units = dict([('p', 10**-12), 
               ('n', 10**-9), 
               ('u', 10**-6), 
               ('m', 10**-3), 
               ('k', 10**3), 
               ('M', 10**6)])

for line in p1.stdout:
   matches = re.findall(r'( -?\d+\.\d*)([pnumkM]?) ', line)
   for (index, (value, unit)) in enumerate(matches):
#      print 'i: %i, v: %s, u: %s, len: %i' % (index, value, unit, len(result))
      value = float(value)
      if len(result) == index:
         result.append([])
      if (unit != ''):
         value = value*units[unit]
      result[index].append(value)

figure(1)
subplot(211)
plot(result[0], result[1], 'gs')
subplot(212)
plot(result[0], result[2], 'gs')
show()

for (values) in result:
   print len(values)

#print 'float: %s, unidade: %s' % (value, unit)
#print '\n'.join([str(number) for number in result[0]])

