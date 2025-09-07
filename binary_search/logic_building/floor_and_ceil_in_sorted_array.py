class Solution:
    def getFloor(self, nums, x):
        n = len(nums)
        low = 0
        high = n - 1
        ans = -1

        # Binary search for floor: greatest element <= x
        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] <= x:
                ans = nums[mid]      # Potential floor found
                low = mid + 1       # Try to find a greater valid value on the right
            else:
                high = mid - 1      # Move left to find a valid value

        return ans
    
    def getCeil(self, nums, x):
        n = len(nums)
        low = 0
        high = n - 1
        ans = -1

        # Binary search for ceil: smallest element >= x
        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] >= x:
                ans = nums[mid]  # Potential ceil found
                high = mid - 1   # Try to find a smaller valid value on the left
            else:
                low = mid + 1    # Move right to find a valid value

        return ans

    def getFloorAndCeil(self, nums, x):
        # Return both floor and ceil as a list
        # Floor: greatest element <= x
        # Ceil: smallest element >= x
        return [self.getFloor(nums, x), self.getCeil(nums, x)]

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))
    x = int(input())

    print(sol.getFloorAndCeil(nums, x))