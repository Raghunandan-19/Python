import math

class Solution:
    def countDigit(self, n):
        # Special case: if the number is 0, it has 1 digit
        if n == 0: 
            return 1

        # Use logarithm to count the number of digits in n
        return int(math.log10(n)) + 1

    def isArmstrong(self, n):
        # Get the number of digits in n
        count = self.countDigit(n)
        dup = n
        sum = 0

        # Iterate over each digit
        while dup > 0:
            last_digit = dup % 10  # Extract the last digit
            sum += pow(last_digit, count)  # Add the digit raised to the power of count
            dup //= 10  # Remove the last digit
        
        # Check if the sum equals the original number
        return (sum == n)
    
if __name__ == "__main__":
    sol = Solution()
    n = int(input())

    print(sol.isArmstrong(n))