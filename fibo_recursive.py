#! /usr/bin/python

def fibo(n):
	a, b = 0, 1
	for i in range(n):
		a, b = b, a + b
		print a,

def fib(n):
	if n == 0 or n == 1 :
		return n 
	else: 
		return fib(n-1) + fib(n-2)