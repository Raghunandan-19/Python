class Solution:
    def findMissingRepeatingNumbers(self, nums):
        n = len(nums)
        # Expected sum of first n natural numbers
        sN = (n * (n + 1)) // 2
        # Expected sum of squares of first n natural numbers
        s2N = (n * (n + 1) * (2 * n + 1)) // 6
        s = 0  # Actual sum of array elements
        s2 = 0 # Actual sum of squares of array elements

        for i in range(n):
            s += nums[i]
            s2 += (nums[i] * nums[i])
        
        # Difference between actual sum and expected sum (repeating - missing)
        val1 = s - sN
        # Difference between actual sum of squares and expected sum of squares (repeating^2 - missing^2)
        val2 = s2 - s2N
        # (repeating^2 - missing^2) / (repeating - missing) = repeating + missing
        val2 //= val1

        # Solve equations to find repeating (x) and missing (y) numbers
        x = (val1 + val2) // 2  # repeating number
        y = x - val1            # missing number

        return [x, y]

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))

    print(sol.findMissingRepeatingNumbers(nums))