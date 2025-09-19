class Solution:
    """ Function to count partitions such 
    that each partition has sum <= maxSum"""
    def countPartitions(self, a, maxSum):
        n = len(a)
        partitions = 1
        subarraySum = 0

        for i in range(n):
            if subarraySum + a[i] <= maxSum:
                # Add element to the current subarray
                subarraySum += a[i]
            else:
                # Start a new subarray with current element
                partitions += 1
                subarraySum = a[i]

        return partitions

    """ Function to find the largest minimum 
    subarray sum with at most k partitions"""
    def largestSubarraySumMinimized(self, a, k):
        # Initialize binary search boundaries
        low = max(a)  
        high = sum(a) 

        # Apply binary search
        while low <= high:
            mid = (low + high) // 2
            partitions = self.countPartitions(a, mid)

            if partitions > k:
                """ If partitions exceed k, increase 
                the minimum possible subarray sum"""
                low = mid + 1
            else:
                """ If partitions are within k, try to 
                minimize the subarray sum further"""
                high = mid - 1

        """ After binary search, 'low' will be
        the largest minimum subarray sum with
        at most k partitions"""
        return low

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    a = list(map(int, input().split()))
    k = int(input())

    print(sol.largestSubarraySumMinimized(a, k))