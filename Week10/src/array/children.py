# validate if node exist based on checking the value existence in the list ls.
def validate(ls, node):
    flag = False
    for i in range(len(ls)):
        if (ls[i] == node):
            flag = True
    return flag

# extract the children based on the given parent.
def extractchildren(ls, node):
    for i in range(len(ls)):
        if (ls[i] == node):
            left = (2*i) + 1
            right = (2*i) + 2
            if (left < len(ls) and right < len(ls)):
                print(ls[left], ",", ls[right])
            else:
                print("no children found")

    
def main():
    ls = [25,15,50,10,22,35,70,4,12,18,24,31,44,66,90]
    parent = int(input("Enter the parent value: "))
    if (validate(ls, parent)):
        print("children:")
        extractchildren(ls, parent)
    else:
        print("Invalid input. Try again ...")
    
if __name__ == "__main__":
    main()
