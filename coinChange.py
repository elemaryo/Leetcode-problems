def combinations(amount, coins: list):
    result = []

    def dfs(amount, coins, i, path, result):

        if i >= len(coins):
            return

        if amount < 0:  # invalid base
            return

        if amount == 0:  # valid case
            result.append([a for a in path])
            return

        # general case
        # call left child
        path.append(coins[i])
        dfs(amount-coins[i], coins, i, path, result)
        path.pop()

        # call right child
        dfs(amount, coins, i+1, path, result)

    dfs(amount, coins, 0, [], result)
    print(result)
#     return min(result)


combinations(20, [5, 10, 20])


def shorestCombination(amount, coins: list):

    def dfs(amount, coins, i, length) -> int:

        if i >= len(coins):
            return 10000

        if amount < 0:  # invalid base
            return 10000

        if amount == 0:  # valid case
            return length

        # general case
        # call left child
        length += 1
        left = dfs(amount-coins[i], coins, i, length)
        length -= 1

        # call right child
        right = dfs(amount, coins, i+1, length)

        return min(left, right)

    return dfs(amount, coins, 0, 0)


print(shorestCombination(20, [5, 10, 20]))

# Time Complexity: O(2^n) where n is the number of input (coins)
# Space Complexity: O(h) where h (amount) is the height of the tree
