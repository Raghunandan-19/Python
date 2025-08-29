class Solution:
    def partition(self, nums, low, high):
        # Choose the first element as the pivot
        pivot = nums[low]
        i = low
        j = high

        # Loop until the two pointers meet
        while i < j:
            # Move i to the right as long as nums[i] <= pivot
            while (nums[i] <= pivot) and (i < high):
                i += 1
            
            # Move j to the left as long as nums[j] > pivot
            while (nums[j] > pivot) and (j >= low + 1):
                j -= 1
            
            # Swap elements at i and j if i < j
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
        
        # Place the pivot in its correct sorted position
        nums[low], nums[j] = nums[j], nums[low]

        # Return the index of the pivot
        return j

    def quickSortHelper(self, nums, low, high):
        # Check if the current subarray has more than one element
        if low <= high:
            # Partition the array and get the index of the pivot after partitioning
            partition_index = self.partition(nums, low, high)
            # Recursively sort the left subarray
            self.quickSortHelper(nums, low, partition_index - 1)
            # Recursively sort the right subarray
            self.quickSortHelper(nums, partition_index + 1, high)
    
    def quickSort(self, nums):
        # Call the helper function to sort the entire list
        self.quickSortHelper(nums, 0, len(nums) - 1)
        # Return the sorted list
        return nums

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))

    print(sol.quickSort(nums))