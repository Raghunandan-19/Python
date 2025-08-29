class Solution:
    def insertionSort(self, nums):
        n = len(nums)  # Get the length of the input list

        # Traverse through all elements in the list
        for i in range(0, n):
            j = i

            # Move elements of nums[0..i-1], that are greater than nums[i],
            # to one position ahead of their current position
            while (j > 0) and (nums[j - 1] > nums[j]):
                nums[j - 1], nums[j] = nums[j], nums[j - 1]  # Swap if the element found is greater
                j -= 1  # Move to the previous element
        
        return nums  # Return the sorted list

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))

    print(sol.insertionSort(nums))