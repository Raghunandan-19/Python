class Solution:
    def largestDigit(self, n):
        # Initialize largest to negative infinity to ensure any digit will be larger
        largest = -float('inf')

        # Loop through each digit in the number
        while n > 0:
            last_digit = n % 10  # Extract the last digit
            
            # Update largest if the current digit is greater
            if last_digit > largest:
                largest = last_digit
            
            n //= 10  # Remove the last digit
        
        # If no digits were found (e.g., n was 0), return 0; otherwise, return the largest digit
        return 0 if largest == -float('inf') else largest

if __name__ == "__main__":
    sol = Solution()
    n = int(input())

    print(sol.largestDigit(n))