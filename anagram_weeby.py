#!/usr/bin/env python

def anagram(data):
	anagrams = ''
	with open("words.lst") as f:
		data = list(f.read())
		if data:
			#return data.reverse()
			anagrams += "{0}\n".format(data[::-1])
	return anagrams

def webby_numbers(n):
	start = 1
	prime_factors = [2, 3, 5]
	primes = [1]
	for i in xrange(start, n):
		if len(primes) >= 1200: break
		prime = False
		for num in prime_factors:
			if (i % num) == 0:
				prime = True
		if prime:
			primes.append(i)
		i += 1
	#print "length of sequence: {0}\ncontent of list: {1}".format(len(primes), primes)
	return primes[-1]
	
def Sum(arg):
	#return sum(n)
	#return n[0] + add(n[1:]) if len(n) > 1 else n[0]
	if not arg: return 0
	return arg[len(arg)-1] + Sum(arg[1:])


def get_function():
	print "inside get_function"                 
	def returned_function():                    
		print "inside returned_function"        
		return 1
	print "outside returned_function"
	return returned_function

def time_this(original_function):                            
	def new_function(*args,**kwargs):                        
		before = datetime.datetime.now()                     
		x = original_function(*args,**kwargs)                
		after = datetime.datetime.now()                      
		print "Elapsed Time = {0}".format(after-before)      
		return x                                             
	return new_function()   

if __name__ == "__main__":
	anag = 'fabiano'
	webby = 3000
	add_list = [7,7,7,7,7,7,7]
	#print(anagram(anag))
	#print(webby_numbers(webby))
	#print(sum(add_list))
	
	# --------------

	#returned_function()     # A                         
	x = get_function()      # B                         
	x                       # C                        
	x()                     # D       
	

