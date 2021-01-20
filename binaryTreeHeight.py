class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = Node(4)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)
root.right = Node(8)
root.right.left = Node(6)
root.right.left.left = Node(5)
root.right.left.left.left = Node(10)
root.right.left.right = Node(7)
root.right.right = Node(9)


'''
                4    root
            2        8
        1     3    6    9
                  5 7   
'''


def height(root) -> int:

    if not root:
        return 0

    else:
        L = height(root.left)  # root = node(8), root.left = node(6), L = 4
        R = height(root.right)  # height(node(9)), R = 3

        ans = L + R + 1
        # ans = max(L, R) + 1  # ans = 3

    return ans


print(height(root))

# Time Complexity: O(N) - Visit all nodes in the tree
# Space Complexity: O(h) - height of the tree for call stack
