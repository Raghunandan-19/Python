class Solution: 
    def reverseString(self, s):
        n = len(s)  # Get the length of the list

        left = 0  # Initialize left pointer
        right = n - 1  # Initialize right pointer

        # Swap characters from both ends moving towards the center
        while left < right:
            s[left], s[right] = s[right], s[left]  # Swap the elements
            left += 1  # Move left pointer to the right
            right -= 1  # Move right pointer to the left

if __name__ == "__main__":
    sol = Solution()
    s = list(input())

    sol.reverseString(s)
    
    print(''.join(s))