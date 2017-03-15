#include <stdio.h>
#include <cs50.h>

int main(void)
{
    printf("How many minutes does your shower take? :");
    int minutes = get_int();
    printf("Minutes: %i\n", minutes);
    printf("Bottles: %i\n", minutes * 12);
}
