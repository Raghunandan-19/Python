import math

class Solution:
    def divisors(self, n):
        # Initialize an empty list to store divisors
        divisor = []

        # Iterate from 1 to the square root of n (inclusive)
        for i in range(1, int(math.sqrt(n) + 1)):
            # If i divides n evenly, it is a divisor
            if n % i == 0:
                divisor.append(i)

                # If i and n//i are different, add n//i as well
                if i != (n // i):
                    divisor.append(n // i)
        
        # Sort the list of divisors in ascending order
        divisor.sort()

        # Return the list of divisors
        return divisor

if __name__ == "__main__":
    sol = Solution()
    n = int(input())

    print(sol.divisors(n))