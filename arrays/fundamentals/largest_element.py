class Solution:
    def largestElement(self, nums):
        n = len(nums)  # Get the number of elements in the list
        largest_number = -float("inf")  # Initialize with the smallest possible value

        # Iterate through each element in the list
        for i in range(n):
            # Update largest_number if current element is greater
            largest_number = max(largest_number, nums[i])
        
        return largest_number  # Return the largest element found

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))

    print(sol.largestElement(nums))