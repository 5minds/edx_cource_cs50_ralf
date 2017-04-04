import sys
import cs50

def main():
    if sanityCheck(len(sys.argv), sys.argv[1]) == False:
        print("Usage: ./vigenere k.")
        return 1
    
    s = getMessage()
    keyLength = len(sys.argv[1])
    encryptKey = argvToKey(sys.argv[1])
    encryptMessage(s, encryptKey, keyLength)

def argvToKey(argvKey):
    newArgvKey = []
    for character in argvKey:
        if character.isalpha:
            newArgvKey.append(ord(character.upper()) - 65)
    return newArgvKey

def encryptMessage(msg, key, keyLength):
    ciphertext = ""
    tmptxt = 0
    n = 0;
    
    for character in msg:
        if character.isalpha:
            tmptxt = ord(character)
            if character <= 'Z' and tmptxt + key[n % keyLength] > 90:
                tmptxt -= 26;
            if character <= 'z' and tmptxt + key[n % keyLength] > 122:
                tmptxt -= 26;
            ciphertext += (chr(tmptxt + key[n % keyLength]))
            n += 1
    
    
    print("ciphertext: {}".format(ciphertext));

def sanityCheck(argumentCount, parameter):
    if argumentCount != 2:
        return False
    for i in range(len(parameter)):
        if parameter[i].isalpha == False:
           return False
    return True

def getMessage():
    print("plaintext: ", end = "")
    s = cs50.get_string()
    n = 0;
    while s[n].isalpha == False and s[n] != ' ':
        print("Invalid input, try again: ", end = "")
        s = cs50.get_string()
        n +=1
    return s

if __name__ == "__main__":
    main()
    