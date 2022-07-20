#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int add(int, int);
//blink 72 day 11
//sum of 2 integers: given two integers a and b, return the sum of the two integers without using the operators + and -.
//constraints: -1000 <= a, b <= +1000

int main(void)
{
    printf("The sum of a and b = %d", add(2, 2));
}
int add(int a, int b) //function definition
{
 return printf("%*c%*c", a, ' ', b, ' ');
}