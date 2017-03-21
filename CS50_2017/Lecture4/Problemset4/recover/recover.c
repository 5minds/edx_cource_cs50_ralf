#include <stdio.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        fprintf(stderr, "Usage: ./recover infile\n");
        return 1;
    }
    
    typedef uint8_t  BYTE;
    BYTE buffer[512];
    char *rawFile = argv[1];
    char printBuffer[10];
    int counter = 0;
    sprintf(printBuffer,"%03d.jpg", counter);
        
        
    FILE *inptr = fopen(rawFile, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", rawFile);
        return 2;
    }
    
    FILE *outptr = fopen("emptyspace", "w");
    
    while (fread(buffer, 1, 512, inptr) == 512)
    {
        if(buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff)
        {
            if(buffer[3] >= 0xe0 && buffer[3] <= 0xef)
            {
                sprintf(printBuffer,"%03d.jpg", counter);
                outptr = fopen(printBuffer, "w");
                counter ++;
            }
        }
        fwrite(buffer, 1, 512, outptr);
    }
    fclose(outptr);
    
    remove ("emptyspace");
    
    fclose(inptr);
}
