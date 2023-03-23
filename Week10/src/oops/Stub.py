from BST import BST 
def main():
    ls = [12, 6, 18, 19, 21, 11, 3, 5, 4, 24, 18]
    bst = BST()
    for item in ls:
    	bst.insert(item)
    print("inorder:")
    print(bst.inorder([]))
    #print("4 search:")
    #print(bst.search(4))
if __name__ == "__main__":
	main()