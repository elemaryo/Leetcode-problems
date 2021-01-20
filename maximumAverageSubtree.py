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
root.right.left.right = Node(7)
root.right.right = Node(9)

'''
                4
            2        8
        1     3    6    9
                  5 7
'''


def driver(root) -> int:
    global avg
    avg = 0
    def dfs(root) -> tuple:  # (total, size)

        if not root:
            return 0, 0

        l = dfs(root.left)
        r = dfs(root.right)
        total = root.val + l[0] + r[0]
        size = 1 + l[1] + r[1]
        global avg
        avg = max(avg, total/size)
        return total, size

    dfs(root)
    return avg


print(driver(root))
# print(dfs(root))
