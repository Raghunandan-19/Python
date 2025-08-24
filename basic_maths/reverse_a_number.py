class Solution:
    def reverseNumber(self, n):
        reversed_number = 0  # Initialize the reversed number to 0

        while n > 0:
            last_digit = n % 10  # Extract the last digit of n
            n //= 10  # Remove the last digit from n
            reversed_number = (reversed_number * 10) + last_digit  # Append last_digit to reversed_number
        
        return reversed_number  # Return the reversed number

if __name__ == "__main__":
    sol = Solution()
    n = int(input())

    print(sol.reverseNumber(n))