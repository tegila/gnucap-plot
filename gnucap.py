from subprocess import *
import re

class gnucap:
   units = dict([('p', 10**-12), 
               ('n', 10**-9), 
               ('u', 10**-6), 
               ('m', 10**-3), 
               ('k', 10**3), 
               ('M', 10**6)])

   def __init__(self):
      pass

   def run(self):
      self.pipe = Popen(['gnucap -b ' + self.filename], shell=True, stdout=PIPE)

   def parse(self):
      self.result = []
      for line in self.pipe.stdout:
         matches = re.findall(r'( -?\d+\.\d*)([pnumkM]?) ', line)
         for (index, (value, unit)) in enumerate(matches):
            value = float(value)
            if len(self.result) == index:
               self.result.append([])
            if (unit != ''):
               value = value*self.units[unit]
            self.result[index].append(value)
            print value

