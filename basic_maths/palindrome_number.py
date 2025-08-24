class Solution:
    def reverseNumber(self, n):
        # Initialize the reversed number to 0
        reversed_number = 0

        # Loop until all digits are processed
        while n > 0:
            # Extract the last digit
            last_digit = n % 10

            # Remove the last digit from n
            n //= 10
            
            # Append the last digit to the reversed number
            reversed_number = (reversed_number * 10) + last_digit
        
        # Return the reversed number
        return reversed_number

    def isPalindrome(self, n):
        # Check if the reversed number is equal to the original number
        return (self.reverseNumber(n) == n)

if __name__ == "__main__":
    sol = Solution()
    n = int(input())

    print(sol.isPalindrome(n))