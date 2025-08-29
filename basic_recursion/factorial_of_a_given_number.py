class Solution:
    def factorial(self, n):
        if n <= 1:
            # Base case: factorial of 0 or 1 is 1
            return 1
        
        # Recursive case: n! = n * (n-1)!
        return n * self.factorial(n - 1)

if __name__ == "__main__":
    sol = Solution()
    n = int(input())

    print(sol.factorial(n))