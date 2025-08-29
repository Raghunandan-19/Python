class Solution:
    def addDigits(self, num):
        # Base case: if the number is a single digit, return it
        if num < 10:
            return num
        
        sum = 0

        # Sum the digits of the number
        while num > 0:
            current_digit = num % 10  # Get the last digit
            sum += current_digit      # Add it to the sum
            num //= 10                # Remove the last digit
        
        # Recursively call addDigits on the sum of digits
        return self.addDigits(sum)

if __name__ == "__main__":
    sol = Solution()
    num = int(input())

    print(sol.addDigits(num))