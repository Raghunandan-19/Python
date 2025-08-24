class Solution:
    def countDigit(self, n):
        # If n is a single digit, return 1
        if n < 10:
            return 1

        count = 0

        # Loop to count the number of digits
        while n > 0:
            count += 1      # Increment count for each digit
            n //= 10        # Remove the last digit
        
        return count        # Return the total count of digits

if __name__ == "__main__":
    sol = Solution()
    n = int(input())

    print(sol.countDigit(n))