#include <stdio.h>
#include <cs50.h>

void makePyramid(int n);
void makeSpace(int n);
void makeBlock(int n);

int main(void)
{
    int height = -1;
    while (height < 0 || height > 23)
    {
        printf("Height :");
        height = get_int();
    }
    makePyramid(height);
}

void makePyramid(int n)
{
    for (int i = 0; i < n; i++)
    {
        makeSpace(n - (i + 1));
        makeBlock(i + 2);
        printf("\n");
    }
}

void makeSpace(int n)
{
    for (int i = 0 ; i < n; i++)
    {
        printf(" ");
    }
}

void makeBlock(int n)
{
    
    for (int i = 0 ; i < n; i++)
    {
        printf("#");
    }
}