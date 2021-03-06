//The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

//Find the sum of all the primes below two million.

//An optimized sieve of Aristophenes(?)

#include <stdio.h>

//why is this in c#?

int main(){
	public int[] ESieve(int upperLimit) {
    	int sieveBound = (int)(upperLimit - 1) / 2;
    	int upperSqrt = ((int)Math.Sqrt(upperLimit) - 1) / 2;
 
    	BitArray PrimeBits = new BitArray(sieveBound + 1, true);
 
    	for (int i = 1; i <= upperSqrt; i++) {
        	if (PrimeBits.Get(i)) {
            	for (int j = i * 2 * (i + 1); j <= sieveBound; j += 2 * i + 1) {
                	PrimeBits.Set(j, false);
            	}
        	}
    	}
 
    	List<int> numbers = new List<int>((int)(upperLimit / (Math.Log(upperLimit) - 1.08366)));
    	numbers.Add(2);
 
    	for (int i = 1; i <= sieveBound; i++) {
        	if (PrimeBits.Get(i)) {
            	numbers.Add(2 * i + 1);
        	}
    	}
 
    	return numbers.ToArray();
	}
}
