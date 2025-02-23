class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def search(root,key):
    temp = root
    while temp:
        if temp.data == key:
            return True
        elif key < temp.data:
            temp = temp.left
        else:
            temp = temp.right
    return False

def insert(root,value):
    if root is None:
        new_node = TreeNode(value)
        root  = new_node
        return root
    if value < root.data:
        root.left = insert(root.left,value)
    else:
        root.right = insert(root.right,value)
    return root

#o(log N)
#O(log N)
def inorder_rec(root):
    if root is None:
        return None

    inorder_rec(root.left)
    print(root.data,end=' ')
    inorder_rec(root.right)


root = None

root = insert(root,5)
root = insert(root,6)
root = insert(root,10)
root = insert(root,4)
root = insert(root,2)
root = insert(root,9)
root = insert(root,8)
root = insert(root,1)

inorder_rec(root)
print()

result = search(root,9)

print(result)