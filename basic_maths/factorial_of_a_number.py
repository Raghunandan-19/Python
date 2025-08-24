class Solution:
    def factorial(self, n):
        # If n is 0, the factorial is 1
        if n == 0: 
            return 1

        # Initialize result variable
        fact = 1

        # Multiply fact by each number from 1 to n
        for i in range(1, (n + 1)):
            fact *= i
        
        # Return the computed factorial
        return fact

if __name__ == "__main__":
    sol = Solution()
    n = int(input())

    print(sol.factorial(n))