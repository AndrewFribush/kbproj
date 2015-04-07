//By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

//What is the 10001st prime number?

int lim = 10001;
int counter = 1;
bool isPrime;
int i;

List<int> primes = new List<int>();
 
primes.Add(2);
 
while(primes.Count < lim){
    counter += 2;
    i = 0;
    isPrime = true;
    while (primes[i]*primes[i] <= counter) {
        if (counter % primes[i] == 0) {
            isPrime = false;
            break;
        }
        i++;
    }
    if (isPrime) {
        primes.Add(counter);
    }
}
