class Solution:
    def sortZeroOneTwo(self, nums):
        n = len(nums)
        low = 0       # Pointer for next position of 0
        mid = 0       # Current element to check
        high = n - 1  # Pointer for next position of 2

        # Traverse the array and sort 0s, 1s, and 2s
        while mid <= high:
            if nums[mid] == 0:
                # Swap current element with low pointer and move both pointers forward
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # If element is 1, just move mid pointer forward
                mid += 1
            else:
                # If element is 2, swap with high pointer and move high pointer backward
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))

    sol.sortZeroOneTwo(nums)

    print(nums)