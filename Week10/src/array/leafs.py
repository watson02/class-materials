def extractleafs(ls):
    for i in range(len(ls)):
       left = 2*i+1
       right = 2*i+2
       if left >= len(ls) and right >= len(ls):
           print(ls[i], " ", end='')
           

def main():
    ls = [25,15,50,10,22,35,70,4,12,18,24,31,44,66,90]
    print("leafs:")
    extractleafs(ls)
    print()
    
if __name__ == "__main__":
    main()