class Solution:
    def reverse(self, nums, left, right):
        # Base case: if the left index is greater than or equal to right, stop recursion
        if left >= right:
            return
        
        # Swap the elements at the left and right indices
        nums[left], nums[right] = nums[right], nums[left]

        # Recursively reverse the subarray between the next pair of indices
        self.reverse(nums, left + 1, right - 1)

    def reverseArray(self, nums):
        # Call the helper function to reverse the array in place
        self.reverse(nums, 0, (len(nums) - 1))
        # Return the reversed array
        return nums

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))

    print(sol.reverseArray(nums))