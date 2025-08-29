class Solution:
    def sorted(self, nums, i):
        # Base case: if we've reached the end of the array, it's sorted
        if i >= len(nums):
            return True
        
        # If the previous element is greater than the current, array is not sorted
        if nums[i - 1] > nums[i]:
            return False
        
        # Recurse for the next pair
        return self.sorted(nums, (i + 1))

    def isSorted(self, nums):
        # Start the recursion from the first index (comparing nums[0] and nums[1])
        return self.sorted(nums, 1)

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))

    print(sol.isSorted(nums))