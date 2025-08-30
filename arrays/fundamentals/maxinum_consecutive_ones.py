class Solution:
    def findMaxConsecutiveOnes(self, nums):
        # Initialize variables to keep track of the maximum number of consecutive ones
        max_ones = 0
        ones = 0

        # Iterate through the list of numbers
        for i in range(len(nums)):
            if nums[i] == 1:
                # Increment the current count of consecutive ones
                ones += 1
                # Update the maximum if the current count is greater
                max_ones = max(ones, max_ones)
            else:
                # Reset the current count if a zero is encountered
                ones = 0
        
        # Return the maximum number of consecutive ones found
        return max_ones

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))

    print(sol.findMaxConsecutiveOnes(nums))