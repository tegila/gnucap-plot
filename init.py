#!/usr/bin/python

from Action import *
from optparse import OptionParser

def main():
	#modulo option parser do python para facilitar a vida
	parser = OptionParser("usage: %prog [options] -f circuitfile", version="%prog 1.0")
	parser.add_option("-f", "--file", dest="filename", 
						help="input circuit file", metavar="FILE")
	parser.add_option("-p", "--param", action="append", type="string", dest="param")
	parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")
	(options, args) = parser.parse_args()
	
	#depois de determinar os parametros de execucao, inicia-se a iteracao por Action
	act = Action()
	act.simulate(options.filename)

if __name__ == "__main__":
	main()

