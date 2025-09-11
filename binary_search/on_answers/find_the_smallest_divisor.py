import math

class Solution:
    """ Helper function to find the 
    summation of division values"""
    def sumByD(self, nums, limit):
        # Size of array
        n = len(nums)  
        
        # Find the summation of division values
        sum_val = 0
        for num in nums:
            sum_val += math.ceil(num / limit)
        return sum_val

    # Function to find the smallest divisor
    def smallestDivisor(self, nums, limit):
        n = len(nums)
        if n > limit:
            return -1
        
        # Initialize binary search bounds
        low = 1
        high = max(nums)

        # Apply binary search
        while low <= high:
            mid = (low + high) // 2
            if self.sumByD(nums, mid) <= limit:
                high = mid - 1
            else:
                low = mid + 1
        #Return the answer
        return low

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))
    limit = int(input())

    print(sol.smallestDivisor(nums, limit))