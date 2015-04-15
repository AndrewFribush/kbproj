//A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

//a**2 + b**2 = c**2
//For example, 32 + 42 = 9 + 16 = 25 = 52.

//There exists exactly one Pythagorean triplet for which a + b + c = 1000.
//Find the product abc.

//Very simple brute force. I should make it more elegant at some point, but this works fine since the operation is simple.

#include <stdio.h>

int main(){
    int a = 0, b = 0, c = 0, found = 0;
    int sum = 1000;

    for (a = 1; a < (sum / 3); a++) {
        for (b = a; b < (sum / 2); b++) {
            c = (sum - a - b);
 
            if ((a * a) + (b * b) == (c * c)) {
                found = 1;
                break;
            }
        }
 
        if (found == 1) {
            break;
        }
    }
    return c;
}
