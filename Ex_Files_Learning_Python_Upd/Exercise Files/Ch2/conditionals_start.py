#
# Example file for working with conditional statements
#


def main():
    x, y = 10, 100

    # conditional flow uses if, elif, else
    if (x < y):
        st = "x is less than y"
        print(st)
    elif (x == y):
        st = "x is equal to y"
    else:
        st = "x is greater than y"
    # conditional statements let you use "a if C else b"
#st = ("x is less than y") if (x < y) else ("x is greater than y or equal to y")

    x = 42
    y = 73
    if x<y: 
        print(f'x < y: x is {x} and y is {y}')
    elif x>y:
        print(f'x > y: x is {x} and y is {y}')
    else:
        print("Get funky with it")


if __name__ == "__main__":
    main()
