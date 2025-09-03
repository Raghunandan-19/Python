class Solution:
    def maxSubArray(self, nums):
        n = len(nums)
        max_sum = -float("inf")  # Initialize max_sum to negative infinity

        # Iterate over all possible starting indices of subarrays
        for i in range(n):
            sum = 0  # Initialize sum for the current subarray
            
            # Iterate over all possible ending indices for the current starting index
            for j in range(i, n):
                sum += nums[j]  # Add current element to sum
                max_sum = max(sum, max_sum)  # Update max_sum if current sum is greater
        
        return max_sum  # Return the maximum subarray sum found

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))

    print(sol.maxSubArray(nums))