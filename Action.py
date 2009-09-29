from gnucap import *

class Action:
   def __init__(self):
      self.data = []
   def setParam(self, param):
      print param
   def simulate(self, filename):
      simulator = gnucap()
      simulator.filename = filename
      simulator.run()
      simulator.parse()
   def plot(self):
      pass

