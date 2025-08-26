class Solution:  
    def largeOddNum(self, s):
        idx = -1  # Initialize idx to -1 to indicate no odd digit found yet

        # Iterate from the end of the string to the beginning
        for i in range((len(s) - 1), -1, -1):
            if (int(s[i]) % 2) == 1:  # Check if the digit is odd
                idx = i  # Store the index of the last odd digit
                break  # Stop at the first (rightmost) odd digit found
        
        i = 0
        # Skip leading zeros up to the found odd digit
        while i <= idx and s[i] == '0':
            i += 1

        # Return the substring from the first non-zero digit to the last odd digit
        return s[i : (idx + 1)]

if __name__ == "__main__":
    sol = Solution()
    s = str(input())

    print(sol.largeOddNum(s))