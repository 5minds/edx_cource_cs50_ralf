import sys
import cs50

def main():
    height = -1
    while height < 0 or height > 23:
        print("Height : ", end = "")
        height = cs50.get_int()
    makePyramid(height)

def makePyramid(n):
    for i in range(n):
        makeSpace(n - (i + 1))
        makeBlock(i + 2)
        print("")

def makeSpace(n):
    for i in range(n):
        print(" ", end = "")

def makeBlock(n):
    for i in range(n):
        print("#", end = "")
        
if __name__ == "__main__":
    main()
    