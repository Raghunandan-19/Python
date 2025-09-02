class Solution:
    def twoSum(self, nums, target):
        n = len(nums)  # Get the length of the input list

        mpp = {}  # Dictionary to store number and its index

        for i in range(n):
            num = nums[i]  # Current number

            more_needed = target - num  # The number needed to reach the target
            
            # Check if the needed number is already in the dictionary
            if more_needed in mpp:
                return [mpp[more_needed], i]  # Return indices of the two numbers
            
            mpp[num] = i  # Store the current number with its index
        
        return [-1, -1]  # Return [-1, -1] if no solution is found

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))

    target = int(input())

    print(sol.twoSum(nums, target))