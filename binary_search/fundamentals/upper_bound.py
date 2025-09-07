class Solution:
    def upperBound(self, nums, x):
        n = len(nums)  # Get the length of the input list
        low = 0
        high = n - 1
        ans = n  # Default answer is n (if no element is greater than x)

        # Binary search to find the upper bound
        while low <= high:
            mid = low + (high - low) // 2  # Find the middle index
            
            if nums[mid] > x:
                ans = mid  # Update answer if current element is greater than x
                high = mid - 1  # Search in the left half
            else:
                low = mid + 1  # Search in the right half
        
        return ans  # Return the index of the upper bound

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))
    x = int(input())

    print(sol.upperBound(nums, x))