from math import sqrt

limit = 100000000;
sqrtLimit = math.sqrt(limit);
summ = 0;
listt = []
 
for (int i = 1; i <= sqrtLimit; i++) {
    int number = i*i;
    for (int j = i + 1; j <= sqrtLimit; j++) {
        number += j * j;
        if (number > limit) break;
 
        if (IsPalindrome(number) && !listt.Contains(number) ) {
            summ += number;
            listt.Add(number);                        
        }
    }
}
