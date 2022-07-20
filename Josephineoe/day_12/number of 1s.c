#include <stdlib.h>
#include <math.h>
//not correct ooo
//day 12 number 1 being
int main()
{
char x; //let x be in its decimal conversion
char ans;

printf("input decimal x: ");
scanf("%d", &x);

printf("x: %d\n", x);

ans = (x%2);
x = x >> 1;
printf("number of '1' bit: %d", ans);

    return ans;
}
