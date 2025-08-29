class Solution:
    def selectionSort(self, nums):
        n = len(nums)  # Get the length of the list

        # Traverse through all elements in the list
        for i in range(n):
            mini = i  # Assume the current index is the minimum

            # Find the minimum element in the remaining unsorted array
            for j in range(i + 1, n):
                if nums[j] < nums[mini]:
                    mini = j  # Update index of minimum element
            
            # Swap the found minimum element with the first element of the unsorted part
            nums[i], nums[mini] = nums[mini], nums[i]
        
        return nums  # Return the sorted list

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))

    print(sol.selectionSort(nums))