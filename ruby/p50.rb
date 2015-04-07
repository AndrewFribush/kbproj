#The prime 41, can be written as the sum of six consecutive primes:

#41 = 2 + 3 + 5 + 7 + 11 + 13
#This is the longest sum of consecutive primes that adds to a prime below one-hundred.

#The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

#Which prime, below one-million, can be written as the sum of the most consecutive primes?

#generatePrimes is complete. consecutivePrimeSum always generates a prime number, but not the right one.
require 'mathn'

def generatePrimes(limit)
	i = (0..limit).to_a
	i[0] = i[1] = nil
	i.each { |j| next unless j
		break if j * j > limit
		(j * j).step(limit, j) { |k| i[k] = nil }
	}
	i.compact!
	return i
end

def consecutivePrimeSum(limit)
	#bring in an array of primes to limit
	i = generatePrimes(limit)
	j, ka, kc, t = 0, 0, 0, 0
	while j < limit
		#add the term in i to j
		j += i[(ka + t)]
		#count every time this operation is performed
		ka += 1
		#ignore if the sum isn't prime
		if j.prime?
			#ignore if the number of terms isn't larger than a previous number of terms
			if ka > kc
				#set ka as the next kc
				kc = ka
				#set counter to zero
				ka = 0
				#counter so that i starts at an additional term
				t += 1
				#store j as js
				js = j
			end
		end
	end
	puts js
end

consecutivePrimeSum(100)