/*Test2.c
Simple Adder (adds i to the sum in a loop)
Justin Hai, May 10 2018 */

#include <stdio.h>
#include <stdlib.h>

int main(void){
	int i = 0;
	int sum = 0;

	for(i = 1; i < 11; i++){
		sum += i;
	}
	printf("Sum: %d\n", sum);
	return sum;
}
