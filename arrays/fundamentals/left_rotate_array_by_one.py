class Solution:
    def rotateArrayByOne(self, nums):
        # Store the first element to place it at the end after rotation
        rotate_element = nums[0]

        # Shift each element one position to the left
        for i in range(1, len(nums)):
            nums[i - 1] = nums[i]
        
        # Place the first element at the end of the array
        nums[len(nums) - 1] = rotate_element

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))

    sol.rotateArrayByOne(nums)

    print(nums)