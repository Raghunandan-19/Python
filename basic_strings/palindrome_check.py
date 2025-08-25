class Solution:    
    def palindromeCheck(self, s):
        n = len(s)  # Get the length of the string

        left = 0  # Initialize left pointer
        right = n - 1  # Initialize right pointer

        # Loop until the pointers meet in the middle
        while left < right:
            # If characters at left and right pointers don't match, it's not a palindrome
            if s[left] != s[right]:
                return False
            left += 1  # Move left pointer to the right
            right -= 1  # Move right pointer to the left
        
        # If all characters matched, it's a palindrome
        return True

if __name__ == "__main__":
    sol = Solution()
    s = str(input())

    print(sol.palindromeCheck(s))