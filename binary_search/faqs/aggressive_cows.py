class Solution:
    def canWePlace(self, nums, n, dist, cows):
        cnt_cows = 1  # Place the first cow in the first stall
        last = nums[0]  # Position of the last placed cow

        # Try to place the rest of the cows
        for i in range(1, n):
            # If the current stall is at least 'dist' away from the last placed cow
            if (nums[i] - last) >= dist:
                cnt_cows += 1  # Place another cow
                last = nums[i]  # Update the position of the last placed cow
            
            # If all cows have been placed successfully
            if cnt_cows >= cows:
                return True

        # Not possible to place all cows with at least 'dist' distance
        return False
    
    def aggressiveCows(self, nums, k):
        n = len(nums)
        nums.sort()  # Sort the stall positions

        low = 1  # Minimum possible distance
        high = nums[-1] - nums[0]  # Maximum possible distance

        # Binary search for the largest minimum distance
        while low <= high:
            mid = low + (high - low) // 2  # Try middle distance
            if self.canWePlace(nums, n, mid, k):
                # If possible to place all cows with at least 'mid' distance, try for a bigger distance
                low = mid + 1
            else:
                # Otherwise, try for a smaller distance
                high = mid - 1
        
        return high  # The largest minimum distance possible

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))
    k = int(input())
    
    print(sol.aggressiveCows(nums, k))