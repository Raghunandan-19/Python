class Solution:
    def firstOccurrence(self, nums, target):
        n = len(nums)
        low = 0
        high = n - 1
        ans = -1

        # Binary search to find the first occurrence of target
        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                ans = mid          # Update answer and search left half
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1      # Target is in the right half
            else:
                high = mid - 1     # Target is in the left half

        return ans

    def lastOccurrence(self, nums, target):
        n = len(nums)
        low = 0
        high = n - 1
        ans = -1

        # Binary search to find the last occurrence of target
        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                ans = mid          # Update answer and search right half
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1      # Target is in the right half
            else:
                high = mid - 1     # Target is in the left half
            
        return ans
        
    def searchRange(self, nums, target):
        return [self.firstOccurrence(nums, target), self.lastOccurrence(nums, target)]

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))
    target = int(input())

    print(sol.searchRange(nums, target))