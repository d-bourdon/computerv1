#!/usr/bin/python3

import sys

class Error(Exception):
   """Base class for other exceptions"""
   pass

def show_help():
	print("Error: Wrong usage.\n ./computer.py [your equation]")
	raise Error

def table_equation():
	"""
	Take the arg[1] and place each X in a table coresponding to his power
	:return : list 
	"""

	# Regex without = ([0-9.=\- ]+)(?:\* X\^([0-9])|)
	table = []
	i = 0
	# reading index
	r_i = 0
	# reading stop
	r_s = 0

	try:
		for l in sys.argv[1]:
			if l == '*':


def validate_input():
	# if nb arg is diff than 2 (program + equation)
	if len(sys.argv) != 2:

		# if < 1 show help, else show error
		if len(sys.argv) < 2:
			show_help()
			raise Error
		else:
			print("Error: no valide entry")
			raise Error

def main():
    try:
    	validate_input()
    except Error:
    	return 1

    for arg in sys.argv[1:]:
        print(arg)

if __name__ == "__main__":
    main()