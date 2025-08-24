class Solution:
    def countOddDigit(self, n):
        count_odd = 0  # Initialize counter for odd digits

        while n > 0:
            last_digit = n % 10  # Extract the last digit

            if last_digit % 2 == 1:  # Check if the digit is odd
                count_odd += 1  # Increment counter if odd
            
            n //= 10  # Remove the last digit
        
        return count_odd  # Return the total count of odd digits

if __name__ == "__main__":
    sol = Solution()
    n = int(input())

    print(sol.countOddDigit(n))