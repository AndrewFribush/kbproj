//A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

//a**2 + b**2 = c**2
//For example, 32 + 42 = 9 + 16 = 25 = 52.

//There exists exactly one Pythagorean triplet for which a + b + c = 1000.
//Find the product abc.

//Very simple brute force. I should make it more elegant at some point, but this works fine since the operation is simple.

int a = 0, b = 0, c = 0;
int sum = 1000;
bool found = false;
for (a = 1; a < sum / 3; a++) {
    for (b = a; b < sum / 2; b++) {
        c = sum - a - b;
 
        if (a * a + b * b == c * c) {
            found = true;
            break;
        }
    }
 
    if (found) {
        break;
    }
}
