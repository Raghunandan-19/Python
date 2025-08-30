class Solution:
    def secondLargestElement(self, nums):
        n = len(nums)
        largest = -float("inf")         # Initialize largest to negative infinity
        second_largest = -float("inf")  # Initialize second largest to negative infinity

        for i in range(n):
            if nums[i] > largest:
                # Update second largest before updating largest
                second_largest = largest
                largest = nums[i]
            elif (nums[i] > second_largest) and (nums[i] != largest):
                # Update second largest if current number is between largest and second largest
                second_largest = nums[i]
        
        # If second largest was not updated, return -1
        return -1 if second_largest == -float("inf") else second_largest 

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))

    print(sol.secondLargestElement(nums))