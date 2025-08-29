class Solution:
    def sum(self, nums, i):
        # Base case: if index reaches the end of the list, return 0
        if i == len(nums):
            return 0
        
        # Recursive case: add current element to the sum of the rest
        return sum(nums, (i + 1))

    def arraySum(self, nums):
        # Start the recursive sum from index 0
        return sum(nums, 0)

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))

    print(sol.arraySum(nums))