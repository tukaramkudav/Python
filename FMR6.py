
from functools import  reduce

def main():
    print("Enter number of elements you want to enter:")
    iSize = int(input())

    Data_Input = []

    print("please enter the data")
    for iCnt in range(0,iSize):
        Value = int(input())
        Data_Input.append(Value)
    print("Data is :",Data_Input)

    Data_Filter = list(filter(lambda  No : (No % 2 == 0),Data_Input))

    print("Data after filter :",Data_Filter)

    Data_Map = list(map(lambda No : No * 2,Data_Filter))

    print("Data after map is :",Data_Map)

    Data_redue = reduce(lambda A,B : A + B,Data_Map)

    print("Data After Reduce is :",Data_redue)
    
if __name__ == "__main__":
    main()