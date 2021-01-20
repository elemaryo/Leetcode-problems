def messageCombination(message, wordset):
    result = []
    phone = {'2': ['a', 'b', 'c'],
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']}

    if len(digits) == 0:
        return result

    def dfs(message, wordset, path, result):

        # base case
        if len(message) == 0:
            result.append([a for a in path if wordset.contains(a)])
            return

        # general case

        for i in range(len(phone[message[0]])):
            path.append(phone[message[0]][i])
            dfs(message[1:], wordset, path, result)
            path.pop()
