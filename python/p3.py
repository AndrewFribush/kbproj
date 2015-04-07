#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

#functions but is extremely slow at such a large number
import math

isPrime=lambda x: all(x % i != 0 for i in range(int(x**0.5)+1)[2:])

def primeFactors(num):
	return filter(isPrime, range(num)[2:])[:5]

x = primeFactors(6008)
print(x[len(x)-1])
