/**
 * helpers.c
 *
 * Helper functions for Problem Set 3.
 */
 
#include <cs50.h>

#include <stdio.h>

#include "helpers.h"

void showResult (int values[], int n);
void bubbleSort(int values[], int n);

/**
 * Returns true if value is in array of n values, else false.
 */
bool search(int value, int values[], int n)
{
    int counter = n/2;
    if (n == 0)
    {
        return false;
    }
    if (value == values[counter])
    {
        return true;
    }
    if (value < values[counter])
    {
        return search(value, values, counter);
    }
    return search(value, values +(n - counter), counter);
}

/**
 * Sorts array of n values.
 */
void sort(int values[], int n)
{
    
    bubbleSort(values, n);
    showResult(values, n);
    return;
}

void showResult (int values[], int n)
{
    int counter = 0;
    while(counter != n)
    {
        printf("%i\n", values[counter]);
        counter++;
    }
}

void bubbleSort(int values[], int n)
{
    int counter1 = 0;
    int counter2 = 0;
    int temp;
    while(counter1 != n)
    {
        counter2 = counter1 + 1;
        while(counter2 != n)
        {
            if(values[counter1] > values[counter2])
            {
                temp = values[counter1];
                values[counter1] = values[counter2];
                values[counter2] = temp;
                temp = 0;
            }
            counter2++;
        }
        counter1++;
    }
}
