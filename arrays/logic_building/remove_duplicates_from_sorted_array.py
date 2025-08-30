class Solution:
    def removeDuplicates(self, nums):
        n = len(nums)  # Get the length of the input list
        unique_element = 0  # Pointer for the position of the last unique element

        # Iterate through the list starting from the second element
        for i in range(1, n):
            # If the current element is different from the last unique element
            if nums[i] != nums[unique_element]:
                nums[unique_element + 1] = nums[i]  # Move the unique element forward
                unique_element += 1  # Increment the unique element pointer
        
        print(unique_element + 1)  # Print the count of unique elements

        # Print the unique elements
        for i in range(unique_element + 1):
            print(nums[i], end=" ")
    
if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))

    sol.removeDuplicates(nums)