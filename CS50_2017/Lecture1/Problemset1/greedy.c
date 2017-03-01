#include <stdio.h>
#include <cs50.h>
#include <math.h>

int getCoin(int n);

int main(void)
{
    int counter = 0;
    float change = -1;
    int cents = 0;
    while (change < 0)
    {
        printf("How much is the change?\n");
        change = get_float();

        cents = roundf(change * 100);
    }
    while (cents != 0)
    {
        cents -= getCoin(cents);
        counter++;

    }
    printf("%i\n", counter);
}

int getCoin(int n)
{
    int result=0;
    if (n >= 25) {
        result = 25;
    } else if (n >= 10) {
        result = 10;
    } else if (n >= 5) {
        result = 5;
    } else if (n >= 1) {
        result = 1;
    }
    return result;
}