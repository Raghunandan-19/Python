class Solution:
    def sumHighestAndLowestFrequency(self, nums):
        n = len(nums)
        max_freq = 0
        min_freq = n 

        mpp = {}  # Dictionary to store frequency of each number

        # Count frequency of each number in nums
        for num in nums:
            if num in mpp:
                mpp[num] += 1
            else:
                mpp[num] = 1
        
        # Find maximum and minimum frequency
        for freq in mpp.values():
            max_freq = max(max_freq, freq)
            min_freq = min(min_freq, freq)
        
        # Return the sum of minimum and maximum frequency
        return (min_freq + max_freq)

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))

    print(sol.sumHighestAndLowestFrequency(nums))