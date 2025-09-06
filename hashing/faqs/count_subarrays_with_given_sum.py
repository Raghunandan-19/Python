class Solution:
    def subarraySum(self, nums, k):
        n = len(nums)  # Get the length of the input array

        mpp = {0 : 1}  # Initialize hashmap to store prefix sums and their counts

        pre_sum = 0    # Initialize prefix sum
        count = 0      # Initialize count of subarrays

        for i in range(n):
            pre_sum += nums[i]  # Update prefix sum
            sum_to_remove = pre_sum - k  # Find the required prefix sum to get sum k
            count += mpp.get(sum_to_remove, 0)  # Add the number of times this sum has occurred
            mpp[pre_sum] = mpp.get(pre_sum, 0) + 1  # Update the count of the current prefix sum
        
        return count  # Return the total count of subarrays

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))
    k = int(input())

    print(sol.subarraySum(nums, k))