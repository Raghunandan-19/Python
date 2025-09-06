class Solution:
    def longestSubarray(self, nums, k):
        n = len(nums)
        pre_sum_map = {}  # Stores prefix sum and its earliest index
        sum = 0           # Current prefix sum
        max_len = 0       # Maximum length of subarray with sum k

        for i in range(n):
            sum += nums[i]  # Update prefix sum

            if sum == k:
                # If sum from 0 to i is k, update max_len
                max_len = max(max_len, i + 1)

                rem = sum - k  # Remainder needed to get sum k

                if rem in pre_sum_map:
                    # If rem was seen before, subarray (pre_sum_map[rem]+1 to i) sums to k
                    length = i - pre_sum_map[rem]
                    max_len = max(max_len, length)
                
                if sum not in pre_sum_map:
                    # Store the earliest index of this prefix sum
                    pre_sum_map[sum] = i
        
        return max_len

if __name__ == "__name__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))
    k = int(input())

    print(sol.longestSubarray(nums, k))