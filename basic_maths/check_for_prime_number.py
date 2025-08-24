import math

class Solution:
    def isPrime(self, n):
        # Numbers less than 2 are not prime
        if n < 2:
            return False
        
        # Check for factors from 2 up to the square root of n
        for i in range(2, int(math.sqrt(n) + 1)):
            # If n is divisible by any number in this range, it's not prime
            if n % i == 0:
                return False

        # If no divisors were found, n is prime
        return True

if __name__ == "__main__":
    sol = Solution()
    n = int(input())

    print(sol.isPrime(n))