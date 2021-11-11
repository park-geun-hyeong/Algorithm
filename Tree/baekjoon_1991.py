import sys 
read = sys.stdin.readline

class Node():
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
                
def preorder(node):
    if node.data is not None:
        print(node.data, end='')
        if node.left is not None:
            preorder(tree[node.left])
        if node.right is not None:
            preorder(tree[node.right])
    
def inorder(node):
    if node.data is not None:
        if node.left is not None:
            inorder(tree[node.left])
        print(node.data, end='')
        if node.right is not None:
            inorder(tree[node.right])
    
def postorder(node):
    if node.data is not None:
        if node.left is not None:
            postorder(tree[node.left])
        if node.right is not None:
            postorder(tree[node.right])
                
        print(node.data, end='')

def print_order(root):
    preorder(root)
    print()
    inorder(root)
    print()
    postorder(root)

if __name__ == "__main__":
    
    n = int(input())  
    tree ={}
    
    for i in range(n):
        data, left ,right = list(map(str, read().split()))
        tree[data] = Node(data, left if left != '.' else None, right if right != '.' else None)
        
    
    print_order(tree['A'])
    
     
