class Solution:
    def lowerBound(self, nums, x):
        n = len(nums)
        low = 0
        high = n - 1
        ans = n  # Default answer if x is greater than all elements

        # Binary search for the lower bound
        while low <= high:
            mid = low + (high - low) // 2  # Prevents overflow

            if nums[mid] >= x:
                ans = mid  # Potential answer found, look for a lower index
                high = mid - 1  # Search left half
            else:
                low = mid + 1  # Search right half
                
        return ans  # Index of the first element >= x, or n if not found

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))
    x = int(input())

    print(sol.lowerBound(nums, x))