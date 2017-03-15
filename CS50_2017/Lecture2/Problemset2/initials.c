#include <stdio.h>
#include <cs50.h>
#include <ctype.h>

string getName(void);
void printInitials(string s);

int main(void)
{
    string name = getName();
    printInitials(name);
}

string getName(void)
{
    string nameString = get_string();
    while(!isalpha(nameString[0]))
    {
        printf("Invalid input, try again: ");
        nameString = get_string();
    }
    nameString[0] = toupper(nameString[0]);
    return nameString;
}

void printInitials(string nameString)
{
    printf("%c", nameString[0]);
    int n = 0;
    while (nameString[n] != '\0')
    {
        if (nameString[n] == ' ')
        {
        nameString[n + 1] = toupper(nameString[n +1]);
        printf("%c", nameString[n + 1]);
        }
        n++;
    }
    printf("\n");
}
