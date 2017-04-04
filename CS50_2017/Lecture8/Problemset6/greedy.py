import sys
import cs50

def main():
    counter = 0;
    change = -1;
    cents = 0;
    while change < 0:
        print("How much is the change?")
        change = cs50.get_float()

        cents = round(change * 100)
    while cents != 0:
        cents -= getCoin(cents)
        counter += 1
    print(counter)

def getCoin(n):
    result = 0
    if n >= 25:
        result = 25
    elif n >= 10:
        result = 10
    elif n >= 5:
        result = 5
    elif n >= 1:
        result = 1
    return result

if __name__ == "__main__":
    main()
    