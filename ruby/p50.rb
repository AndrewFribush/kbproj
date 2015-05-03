#The prime 41, can be written as the sum of six consecutive primes:

#41 = 2 + 3 + 5 + 7 + 11 + 13
#This is the longest sum of consecutive primes that adds to a prime below one-hundred.

#The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

#Which prime, below one-million, can be written as the sum of the most consecutive primes?

#generatePrimes is complete. consecutivePrimeSum always generates a prime number, but not the right one.


#Full of quasi-code, needs to be rubified
lim = 1000000
result = 0
numPrimes = 0
primes = ESieve(1,limit)
primeSum = primes.length + 1

primeSum[0] = 0;

# Need to fix this into ruby for codes
for (int i = 0; i < primes.length; i++):
    primeSum[i+1] = primeSum[i] + primes[i];
end

for (int i = numberOfPrimes; i < primeSum.Length; i++) {
    for (int j = i-(numberOfPrimes+1); j >= 0; j--) {
        if (primeSum[i] - primeSum[j] > limit) break
 
        if (BinarySearch(primes, primeSum[i] - primeSum[j]) >= 0) {
            numberOfPrimes = i - j;
            result = primeSum[i] - primeSum[j];
        }
    }
}
