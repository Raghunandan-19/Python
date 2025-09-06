class Solution:
    def maxProduct(self, nums):
        n = len(nums)
        prefix = 1
        suffix = 1
        max_product = -float("inf")  # Initialize max_product to negative infinity

        for i in range(n):
            # Reset prefix and suffix to 1 if they become 0 (to handle zeros in array)
            if prefix == 0:
                prefix = 1
            
            if suffix == 0:
                suffix = 1
            
            # Multiply prefix with current element from start
            prefix *= nums[i]
            # Multiply suffix with current element from end
            suffix *= nums[n - i - 1]

            # Update max_product with the maximum of current prefix and suffix products
            max_product = max(max_product, max(prefix, suffix))
        
        return max_product  # Return the maximum product found

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))

    print(sol.maxProduct(nums))