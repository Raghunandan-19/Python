import math

class Solution:
    def isPerfect(self, n):
        # 1 is not a perfect number
        if n == 1:
            return False
        
        sum = 0  # Initialize sum of divisors

        # Loop through all numbers from 1 to sqrt(n)
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                sum += i  # Add divisor

            # Add the corresponding divisor if it's not n or a duplicate
            if (n // i != n) and (i != n // i):
                sum += (n // i)

        # Check if sum of divisors equals the number
        return (sum == n)

if __name__ == "__main__":
    sol = Solution()
    n = int(input())

    print(sol.isPerfect(n))