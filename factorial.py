#! /usr/bin/python

def factor(n):
	if n == 0 or n == 1: 
		return n
	else:
		return n * factor(n-1)

if __name__ == "__main__":

	print factor(5)
