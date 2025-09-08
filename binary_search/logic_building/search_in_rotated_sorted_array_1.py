class Solution:
    def search(self, nums, k):
        n = len(nums)
        low = 0
        high = n - 1

        # Perform modified binary search
        while low <= high:
            mid = low + (high - low) // 2

            # Check if mid is the target
            if nums[mid] == k:
                return mid
            
            # Check if the left half is sorted
            if nums[low] <= nums[mid]:
                # If target is in the left half
                if (nums[low] <= k) and (k <= nums[mid]):
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                # Right half is sorted
                # If target is in the right half
                if (nums[mid] <= k) and (k <= nums[high]):
                    low = mid + 1
                else:
                    high = mid - 1
        
        # Target not found
        return -1

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))
    k = int(input())
    
    print(sol.search(nums, k))