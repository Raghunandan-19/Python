class Solution:
    def findKRotation(self, nums):
        n = len(nums)
        low = 0
        high = n - 1
        ans = float("inf")  # Initialize answer as infinity
        idx = -1            # Initialize index of minimum element

        while low <= high:
            mid = low + (high - low) // 2  # Calculate mid index

            # If the subarray is already sorted
            if nums[low] <= nums[high]:
                if (nums[low] < ans):
                    ans = nums[low]
                    idx = low  # Update answer and index with low
                break  # Minimum found, exit loop

            # If left part is sorted
            if nums[low] <= nums[mid]:
                if nums[low] < ans:
                    ans = nums[low]
                    idx = low  # Update answer and index with low
                low = mid + 1  # Search in right half
            else:
                # Right part is sorted or contains the minimum
                if nums[mid] < ans:
                    ans = nums[mid]
                    idx = mid  # Update answer and index with mid
                high = mid - 1  # Search in left half

        return idx  # Return index of minimum element (number of rotations)
    
if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))

    print(sol.findKRotation(nums))