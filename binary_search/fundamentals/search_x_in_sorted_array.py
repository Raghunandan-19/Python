class Solution:
    def search(self, nums, target):
        n = len(nums)
        low, high = 0, n - 1  # Initialize the search boundaries

        while low <= high:
            mid = low + (high - low) // 2  # Find the middle index

            if nums[mid] < target:
                low = mid + 1  # Search in the right half
            elif nums[mid] > target:
                high = mid - 1  # Search in the left half
            else:
                return mid  # Target found at index mid
        
        return -1  # Target not found
    
if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))
    target = int(input())

    print(sol.search(nums, target))