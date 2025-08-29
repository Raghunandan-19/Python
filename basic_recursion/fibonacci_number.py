class Solution:
    def fib(self, n):
        # Base case: if n is 0, return 0
        if n == 0:
            return 0
        # Base case: if n is 1, return 1
        if n == 1:
            return 1
        
        # Recursive case: sum of the previous two Fibonacci numbers
        return self.fib(n - 1) + self.fib(n - 2)

if __name__ == "__main__":
    sol = Solution()
    n = int(input())

    print(sol.fib(n))