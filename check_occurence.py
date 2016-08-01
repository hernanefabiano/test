fruit = 'adasdasdasfdfdgegebbehhgkyohppgggllttororrlsldvbncx,ccvxxxdflfdfexlzmnbtruuueodsowosdsdsd'
occurence = {}
print '\n'
print list(fruit)
print '\n'
for i in range(len(fruit)):
	if fruit[i] not in occurence.iterkeys():
		for j in range(len(fruit)):
			if fruit[i] == fruit[j]:
				if fruit[i] in occurence.iterkeys():
					occurence[fruit[i]] += 1
				else: occurence[fruit[i]] = 1
print occurence


a = list('anagram')
#print '\nanagram'
#print "".join(a[::-1])
#a.reverse()
#print a

def prime(n):
	val1 = ""
	print "-"*30
	print "starting prime with n =", n
	if n == 0:
		print("Equals zero, This is not a Prime number")
		## zero = False
	answer = 0
	if n == 1:
		print("Equals one, This is not a Prime number")
		## one = True but you print that it is not prime
	answer = 1 
	if val1 == 0:
		print("This is not a Prime number, if val1 == 0")
		## use of False, not zero
		answer = False
	else:
		print("This is a prime number, else val1 == 0")
		## use of True, not one
	answer = True

#prime(232121212121)

