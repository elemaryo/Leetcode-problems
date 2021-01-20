class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        return self.fib(N-1) + self.fib(N-2)

# Time Complexity: O(2^n) - you need to look at each level of the tree
# Space Complexit: O(n) - call stack space


# other method

class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        return self.memoize(N)

    def memoize(self, N: int) -> {}:
        cache = {0: 0, 1: 1}

        # Since range is exclusive and we want to include N, we need to put N+1.
        for i in range(2, N+1):
            cache[i] = cache[i-1] + cache[i-2]

        return cache[N]


int fib(int n, int[] memo) {
    if (n == 0 | | n == 1) return n
    if (memo[n] == 0)
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]
}

# Time Complexity: O(n) - completed values are stored and return once new value is discovered
# Space Complexit: O(n) - call stack space
# Videos: https://www.youtube.com/watch?v=vYquumk4nWw&ab_channel=CSDojo

# Iteration
int fib(int n) {
    // Base cases
    if (n == 0) return 0
    else if (n == 1) return 1

    int[] memo = new int[n + 1]
    memo[0] = 0
    memo[0] = 1
    for (int i=2
         i <= n
         i++) {
        memo[i] = memo[i - 1] + memo[i - 2]
    }
    return memo[n] + memo[n - 1]
}

int fib(int n) {
    // Base cases
    if (n == 0) return 0
    else if (n == 1) return 1

    int a = 0
    int b = 1
    for (int i=2
         i < n
         i++) {
        int c = a + b
        a = b
        b = c
    }
    return a + b
}

# Time Complexity: O(n)
# Space Complexity: O(1)
# Links: https://medium.com/@dakota.lillie/an-intro-to-dynamic-programming-pt-i-d782bf81ac51
# https://www.freecodecamp.org/news/an-intro-to-algorithms-dynamic-programming-dd00873362bb/
