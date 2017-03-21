#include <stdio.h>
#include <cs50.h>
#include <ctype.h>

string getMessage(void);
bool sanityCheck(int j, string t);
long argvToInt(string t);
void encryptMessage(string msg, int key);

int main(int argc, string argv[])
{
    if (!sanityCheck(argc, argv[1]))
    {
        printf("Usage: ./caesar k.\n");
        return 1;
    }
    
    int encryptKey = argvToInt(argv[1]);
    
    string message = getMessage();
    encryptMessage(message, encryptKey);
    
}

void encryptMessage(string msg, int key)
{
    while (key < 0)
    {
        key = key + 26;
    }
    
    key = key % 26;
    
    int n = 0;
    while(msg[n] != '\0')
    {
        if(isalpha(msg[n]))
        {
           if(msg[n] <= 'Z' && msg[n] + key > 'Z')
           {
                msg[n] = msg[n] - 26;
           }
           if(msg[n] <= 'z' && msg[n] + key > 'z')
           {
                msg[n] = msg[n] - 26;
           }
                msg[n] = msg[n] + key;
        }
        n++;
    }
    
    printf("ciphertext: %s\n", msg);
}

long argvToInt(string t)
{
    char *p;
    long l = strtol(t, &p, 10);
    return l;
}

bool sanityCheck(int argumentCount, string parameter)
{
    if(argumentCount != 2)
    return false;
    int n = 0;
    while (parameter[n] != '\0')
    {
        if (parameter[0] != '-')
        {
            while(!isdigit(parameter[n]))
            {
                return false;
            }
        }
        n++;
    }
    return true;
}

string getMessage(void)
{
    printf("plaintext: ");
    string msgString = get_string();
    int n = 0;
    while(!isalpha(msgString[n]) && msgString[n] != ' ')
    {
        printf("Invalid input, try again: ");
        msgString = get_string();
        n++;
    }
    return msgString;
}
