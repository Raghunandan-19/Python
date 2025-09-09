class Solution:
    def searchInARotatedSortedArrayII(self, nums, k):
        n = len(nums)
        low = 0
        high = n - 1

        while low <= high:
            mid = low + (high - low) // 2  # Calculate the middle index

            if nums[mid] == k:
                return True  # Target found
            
            # If duplicates are at the ends, skip them
            if (nums[low] == nums[mid]) and (nums[mid] == nums[high]):
                low += 1
                high -= 1
                continue
            
            # Left half is sorted
            if nums[low] <= nums[mid]:
                # Target is in the left half
                if (nums[low] <= k) and (k <= nums[mid]):
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                # Right half is sorted
                if (nums[mid] <= k) and (k <= nums[high]):
                    low = mid + 1
                else:
                    high = mid - 1
        
        return False  # Target not found

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))
    k = int(input())

    print(sol.searchInARotatedSortedArrayII(nums, k))