class Solution:
    def nextPermutation(self, nums):
        n = len(nums)
        idx = -1

        # Find the first index from the end where nums[i] < nums[i + 1]
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                idx = i
                break
        
        # If no such index exists, reverse the entire array (last permutation)
        if idx == -1:
            nums.reverse()
            return 
        
        # Find the smallest number larger than nums[idx] to the right of idx
        for i in range(n - 1, idx - 1, -1):
            if nums[i] > nums[idx]:
                # Swap them
                nums[i], nums[idx] = nums[idx], nums[i]
                break
        
        # Reverse the subarray to the right of idx to get the next permutation
        nums[idx + 1:] = reversed(nums[idx + 1:])
        
        return

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))

    sol.nextPermutation(nums)

    print(nums)