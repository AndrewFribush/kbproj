int limit = 100000000;
double sqrtLimit = Math.Sqrt(limit);
 
long sum = 0;
SortedSet list = new SortedSet();
 
for (int i = 1; i <= sqrtLimit; i++) {
    int number = i*i;
    for (int j = i + 1; j <= sqrtLimit; j++) {
        number += j * j;
        if (number > limit) break;
 
        if (IsPalindrome(number) && !list.Contains(number) ) {
            sum += number;
            list.Add(number);                        
        }
 
    }
}
