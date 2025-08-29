class Solution:
    def isPalindrome(self, s, left, right):
        # Base case: If the left index crosses or meets the right, it's a palindrome
        if left >= right:
            return True
        
        # If characters at current indices don't match, it's not a palindrome
        if s[left] != s[right]:
            return False
        
        # Move towards the center and check the next pair
        return self.isPalindrome(s, left + 1, right - 1)

    def palindromeCheck(self, s):
        # Call the recursive isPalindrome function with initial left and right indices
        return self.isPalindrome(s, 0, (len(s) - 1))

if __name__ == "__main__":
    sol = Solution()
    s = str(input())

    print(sol.palindromeCheck(s))