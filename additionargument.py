from sys import *
def Addition(A,B):
    Ans = 0
    Ans = A + B
    return Ans

def main():
    if(len(argv) != 3):
        print("Invalid number of arguments")
        exit()

    ret = Addition(int(argv[1]),int(argv[2]))

    print("Addition is :",ret)


if __name__ == "__main__":
    main()
