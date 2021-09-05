class TreeNode:
    def __init__(self, val, left=None, right=None, sub_sum = 0):
        self.val = val
        self.left = left
        self.right = right
        self.sub_sum = sub_sum # keeps track of the sum of the subtree
        
def main():
    q = int(input()) # number of nodes
    weights = list(map(int,input().split())) #second line input
    
    #not gonna go in depth but this builds a heap array kind of structure, which i use to build my tree understanding that leftchild = 2i + 1 and rightchild = 2i +2
    tree = [1]
    root = TreeNode(weights[0])
    for i in range (q):
        values = list(map(int,input().split()))
        tree.append(values[0])
        tree.append(values[1])
    # print(tree)
    buildTree(root, 0, len(tree)-1, weights, tree)
    
    #goes through the tree and calculates every subtree sum for each root
    def recurse(root):
        if root == None:
            return 0
        root.sub_sum = root.val + recurse(root.left) + recurse(root.right)
        return root.sub_sum
    recurse(root)
    
    #goes through the tree in preorder traversal and prints that subtree sum
    def recurse1(root):
        if root != None:
            print(root.sub_sum, end = ' ')
            recurse1(root.left)
            recurse1(root.right)
    recurse1(root)
    
def buildTree(root, index, maxLength, weights, values):
    if index * 2 + 1 > maxLength:
        return
    #print(index, index*2+1, values[index*2+1], weights[values[index*2+1]-1])
    weight = 0
    if values[index*2+1] == -1:
        weight = -1
        #dont return in case there is a right child
    else:
        weight = weights[values[index*2+1]-1]
        root.left = TreeNode(weight)
        buildTree(root.left, index*2+1, maxLength, weights, values)

    if index * 2 + 2 > maxLength:
        return
    if values[index*2+2] == -1:
        weight = -1
        return
    else:
        weight = weights[values[index*2+2]-1]
        root.right = TreeNode(weight)
        buildTree(root.right, index*2+2, maxLength, weights, values)

if __name__ == '__main__':
    main()
