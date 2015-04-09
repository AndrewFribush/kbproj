#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

#functions but is extremely slow at such a large number
import math

givenNum = 600851475143

def isPrime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True

def factors(num):    
    return reduce(list.__add__, ([i, num//i] for i in range(1, int(num**0.5) + 1) if num % i == 0))

def primeFactors(num):
	sortedFactors = sorted(factors(num))
	finalList = []
	for i in sortedFactors:
		if isPrime(i):
			finalList.append(i)
	return finalList[len(finalList)-1]

x = primeFactors(givenNum)
print(x)
