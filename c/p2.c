#include <stdio.h>

int main()
{
	int first = 1, second = 2, next, sum = 0;
	while(next < 4000000){
		next = first + second;
		first = first;
		second = next;
		if((next % 2) == 0){
			sum = sum + next;
		} 
	}
	return sum;
}
