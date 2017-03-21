#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>

string getMessage(void);
bool sanityCheck(int argumentCount,string parameter);
void encryptMessage(string msg, string key, int keyLength);
string argvToKey(string argvKey);

int main(int argc, string argv[])
{
    if (!sanityCheck(argc, argv[1]))
    {
        printf("Usage: ./vigenere k.\n");
        return 1;
    }
    
    string s = getMessage();
    int keyLength = strlen(argv[1]);
    string encryptKey = argvToKey(argv[1]);
    encryptMessage(s, encryptKey, keyLength);
}

string argvToKey(string argvKey)
{
    int n = 0;
    
    while(argvKey[n] != '\0')
    {
        if(isalpha(argvKey[n]))
        {
            argvKey[n] = toupper(argvKey[n]);
            argvKey[n] = argvKey[n] - 65;
        }
        n++;
    }
    return argvKey;
}

void encryptMessage(string msg, string key, int keyLength)
{
    int n = 0;
    int n2 = 0;
    
    while(msg[n] != '\0')
    {
        if(isalpha(msg[n]))
        {
           if(msg[n] <= 'Z' && msg[n] + key[n2 % keyLength] > 'Z')
           {
                msg[n] = msg[n] - 26;
           }
           if(msg[n] <= 'z' && msg[n] + key[n2 % keyLength] > 'z')
           {
                msg[n] = msg[n] - 26;
           }
                msg[n] = msg[n] + key[n2 % keyLength];
                n2++;
        }
        n++;
    }
    
    
    printf("ciphertext: %s\n", msg);
}

bool sanityCheck(int argumentCount, string parameter)
{
    if(argumentCount != 2)
    return false;
    int n = 0;
    while (parameter[n] != '\0')
    {
        while(!isalpha(parameter[n]))
        {
           return false;
        }
        n++;
    }
    return true;
}

string getMessage(void)
{
    printf("plaintext: ");
    string s = get_string();
    int n = 0;
    while(!isalpha(s[n]) && s[n] != ' ')
    {
        printf("Invalid input, try again: ");
        s = get_string();
        n++;
    }
    return s;
}
