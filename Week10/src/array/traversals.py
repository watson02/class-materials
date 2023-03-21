def inorder(ls, index):
	if (index >= len(ls)):
		return;
	inorder(ls, (2*index)+1)
	print(ls[index], " ", end = '')
	inorder(ls, (2*index)+2)

def postorder(ls, index):
	if (index >= len(ls)):
		return;
	postorder(ls, (2*index)+1)
	postorder(ls, (2*index)+2)
	print(ls[index], " ", end = '')

def preorder(ls, index):
	if (index >= len(ls)):
		return;
	print(ls[index], " ", end = '')
	preorder(ls, (2*index)+1)
	preorder(ls, (2*index)+2)

def main():
	ls = [25,15,50,10,22,35,70,4,12,18,24,31,44,66,90]
	inorder(ls, 0)
	print()
if __name__ == "__main__":
	main()