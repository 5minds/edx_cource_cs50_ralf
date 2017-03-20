#include <stdio.h>
#include <stdlib.h>

#include "bmp.h"

int main(int argc, char *argv[])
{
    if (argc != 4)
    {
        fprintf(stderr, "Usage: ./resize n(1 to 100) infile outfile\n");
        return 1;
    }
    
    
    int rFactor = atoi(argv[1]);
    char *infile = argv[2];
    char *outfile = argv[3];
    
    printf("this is the resize Factor : %i\n", rFactor);
    
    if (rFactor < 1 || rFactor > 100)
    {
        fprintf(stderr, "n can only be between 1 and 100.\n");
        return 1;
    }

    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 1;
    }

    FILE *outptr = fopen(outfile, "w");
    if (outptr == NULL)
    {
        fclose(inptr);
        fprintf(stderr, "Could not create %s.\n", outfile);
        return 3;
    }

    BITMAPFILEHEADER bf;
    fread(&bf, sizeof(BITMAPFILEHEADER), 1, inptr);

    BITMAPINFOHEADER bi;
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, inptr);

    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 || 
        bi.biBitCount != 24 || bi.biCompression != 0)
    {
        fclose(outptr);
        fclose(inptr);
        fprintf(stderr, "Unsupported file format.\n");
        return 4;
    }

    int padding = (4 - (bi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;
    
    bi.biHeight *= rFactor;
    bi.biWidth *= rFactor;
    
    int newPadding = (4 - (bi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;
    
    
    bi.biSizeImage = ((sizeof(RGBTRIPLE) * bi.biWidth) + newPadding) * abs(bi.biHeight);
    bf.bfSize = bi.biSizeImage + sizeof(BITMAPFILEHEADER) + sizeof(BITMAPINFOHEADER);

    fwrite(&bf, sizeof(BITMAPFILEHEADER), 1, outptr);

    fwrite(&bi, sizeof(BITMAPINFOHEADER), 1, outptr);


    for (int i = 0, biHeight = abs(bi.biHeight); i < biHeight; i++)
    {
        for(int l = 0; l < rFactor; l++)
        {
            // scaling happens in the most inner loop, loop over the original size here, not the new size
            for (int j = 0; j < bi.biWidth / rFactor; j++)
            {
                RGBTRIPLE triple;


                for (int k = 0; k < rFactor; k++)
                {
                    fread(&triple, sizeof(RGBTRIPLE), 1, inptr);
                    fwrite(&triple, sizeof(RGBTRIPLE), 1, outptr);
                    fseek(inptr, -3, SEEK_CUR);
                }
                fseek(inptr, sizeof(RGBTRIPLE), SEEK_CUR);
            }

            for (int m = 0; m < newPadding; m++)
            {
                fputc(0x00, outptr);
            }
            
            fseek(inptr, -3 * bi.biWidth / rFactor, SEEK_CUR);
        }
        
        // Jump to the end of the line (seek above makes the pointer be at the start of the line)
        fseek(inptr, 3 * bi.biWidth / rFactor, SEEK_CUR);
        
        // skip padding from original image (wurde rausgenommen)
        fseek(inptr, padding, SEEK_CUR);
    }

    fclose(inptr);

    fclose(outptr);

    return 0;
}
