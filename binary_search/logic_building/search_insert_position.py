class Solution:
    def searchInsert(self, nums, target):
        n = len(nums)
        low = 0
        high = n - 1
        ans = n  # Default position is at the end if target is greater than all elements

        # Binary search to find the insert position
        while low <= high:
            mid = low + (high - low) // 2  # Calculate mid index

            if nums[mid] >= target:
                ans = mid  # Potential insert position found
                high = mid - 1  # Search left half
            else:
                low = mid + 1  # Search right half
        
        return ans  # Return the insert position

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))
    target = int(input())

    print(sol.searchInsert(nums, target))