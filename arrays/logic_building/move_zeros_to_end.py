class Solution:
    def moveZeroes(self, nums):
        n = len(nums)
        zero_index = -1  # Initialize the index of the first zero to -1

        # Find the index of the first zero in the list
        for i in range(n):
            if nums[i] == 0:
                zero_index = i
                break
        
        # If there are no zeros, return as no changes are needed
        if zero_index == -1:
            return
        
        # Traverse the rest of the list and swap non-zero elements with the zero at zero_index
        for i in range(zero_index + 1, n):
            if nums[i] != 0:
                nums[i], nums[zero_index] = nums[zero_index], nums[i]
                zero_index += 1  # Move zero_index to the next zero position

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))

    sol.moveZeroes(nums)

    print(nums)