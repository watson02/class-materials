# import math library
import math
# validate if node exist based on checking the value existence in the list ls.
def validate(ls, node):
    flag = False
    for i in range(len(ls)):
        if (ls[i] == node):
            flag = True
    return flag

# extract the parent based on the given child value.
def extractgrandparent(ls, node):
    pass

    
def main():
    ls = [25,15,50,10,22,35,70,4,12,18,24,31,44,66,90]
    node = int(input("Enter the grand child node value: "))
    if (validate(ls, node)):
        print("grand parent:")
        extractgrandparent(ls, node)
    else:
        print("Invalid input. Try again ...")
    
if __name__ == "__main__":
    main()
