class Solution:
    def rearrangeArray(self, nums):
        n = len(nums)
        # positive_idx will point to the next position for a positive number (even indices)
        positive_idx = 0
        # negative_idx will point to the next position for a negative number (odd indices)
        negative_idx = 1
        # Initialize the answer array with zeros
        ans = [0] * n
        
        # Iterate through the input array
        for i in range(n):
            if nums[i] > 0:
                # Place positive numbers at even indices
                ans[positive_idx] = nums[i]
                positive_idx += 2
            else:
                # Place negative numbers at odd indices
                ans[negative_idx] = nums[i]
                negative_idx += 2
        
        return ans

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))

    print(sol.rearrangeArray(nums))