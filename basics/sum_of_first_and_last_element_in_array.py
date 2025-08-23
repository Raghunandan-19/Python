class Solution:
    def sumOfFirstAndLast(self, nums):
        if not nums:
            return 0

        return (nums[0] + nums[-1])
    
if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))

    print(nums)
    print(sol.sumOfFirstAndLast(nums))