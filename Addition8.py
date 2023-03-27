print("Application to demonstrate industrial programming")

import MarvellousModule

def main():
    print("Value of __name__ from main is :",__name__)
    print("Enter first Number")
    no1 = int(input())
    print("Enter Second Number")
    no2 = int(input())

    ret = MarvellousModule.Addition(no1,no2)

    print("Addition is :", ret)

if __name__ == "__main__":
    main()
