class Solution:
    def reverse(self, s, left, right):
        # Base case: if the left index is greater than or equal to right, stop recursion
        if left >= right:
            return
        
        # Swap the elements at the left and right indices
        s[left], s[right] = s[right], s[left]

        # Recursively call reverse on the next inner pair
        self.reverse(s, left + 1, right - 1)

    def reverseString(self,s):
        # Call the helper function to reverse the list in place
        self.reverse(s, 0, (len(s) - 1))
        # Return the reversed list
        return s

if __name__ == "__main__":
    sol = Solution()
    s = list(map(str, input().split()))

    print(sol.reverseString(s))