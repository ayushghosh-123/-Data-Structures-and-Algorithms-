class Node :
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

def Insert(root, value):
        if( root == None):
            return Node(value)
        if(root.data == value):
            return root
        if (root.data >value):
           root.left = insert(root.left , value)
        else:
            root.right = insert(root.right, value)

        return root

def Searching(root, value):
        if( root == None):
            print("element not found")
            return
        if(root.data == value):
            print("element found")
            return
        if (root.data >value):
           Searching(root.left , value)
        else:
            Searching(root.right, value)

        return root

def deleteion(root, value):
    if (root == None):
        return root
    elif (root.data > value):
       root.left = deleteion(root.left, value)
    elif (root.data < value):
        root.right = deleteion(root.right , value)

    else:

        if (root.left == None):
            return root.right
        if (root.right == None):
            return root.left 
        else :
            succ = get_succesor(root)
            root.data = succ.data
            root.right = deleteion(root.right, succ.data)
    return root

def get_succesor(root):
    root = root.right
    while (root != None and root.left != None):
        root = root.left
    return root 
 

def InOrder(root):
    if (root != None):
        InOrder(root.left)
        print(root.data , end=' ')
        InOrder(root.right)

root = Insert(None , 20)
root = Insert(root, 15 )
root = Insert(root, 30)
root = Insert(root, 40)
root = Insert(root, 12)
root = Insert(root, 18)
root = Insert(root, 25)
root = Insert(root, 50)

InOrder(root)
