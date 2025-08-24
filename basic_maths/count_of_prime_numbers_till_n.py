import math

class Solution:
    def isPrime(self, n):
        # Numbers less than 2 are not prime
        if n < 2:
            return False
        
        # Check divisibility from 2 up to the square root of n
        for i in range(2, int(math.sqrt(n) + 1)):
            if n % i == 0:  # If divisible, n is not prime
                return False

        # If no divisors found, n is prime
        return True

    def primeUptoN(self, n):
        count = 0  # Initialize count of prime numbers
        
        # Iterate through all numbers from 1 to n (inclusive)
        for i in range(1, (n + 1)):
            if self.isPrime(i):  # Check if the number is prime
                count += 1  # Increment count if prime
        
        return count  # Return the total count of prime numbers

if __name__ == "__main__":
    sol = Solution()
    n = int(input())

    print(sol.primeUptoN(n))