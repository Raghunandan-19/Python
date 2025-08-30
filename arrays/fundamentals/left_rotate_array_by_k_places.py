class Solution:
    def reverse(self, nums, start, end):
        # Reverse the elements in nums from index 'start' to 'end'
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]  # Swap elements
            start += 1  # Move start pointer forward
            end -= 1    # Move end pointer backward

    def rotateArray(self, nums, k):
        n = len(nums)
        k %= n  # Ensure k is within the bounds of the array length

        # Reverse the first k elements
        self.reverse(nums, 0, k - 1)

        # Reverse the remaining n-k elements
        self.reverse(nums, k, n - 1)
        
        # Reverse the entire array to achieve the left rotation
        self.reverse(nums, 0, n - 1)

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))
    k = int(input())

    sol.rotateArray(nums, k)

    print(nums)