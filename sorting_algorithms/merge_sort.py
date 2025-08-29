class Solution:
    def merge(self, nums, low, mid, high):
        # Temporary list to store merged elements
        temp = []
        left = low           # Start index of the left subarray
        right = mid + 1      # Start index of the right subarray

        # Merge the two sorted subarrays into temp
        while (left <= mid) and (right <= high):
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                temp.append(nums[right])
                right += 1
        
        # Copy any remaining elements from the left subarray
        while left <= mid:
            temp.append(nums[left])
            left += 1
        
        # Copy any remaining elements from the right subarray
        while right <= high:
            temp.append(nums[right])
            right += 1

        # Copy the merged elements back into the original array
        for i in range(low, (high + 1)):
            nums[i] = temp[i - low]

    def mergeSortHelper(self, nums, low, high):
        # Base case: if the subarray has one or no elements, it's already sorted
        if low >= high:
            return
        
        # Find the middle point to divide the array into two halves
        mid = low + (high - low) // 2

        # Recursively sort the first half
        self.mergeSortHelper(nums, low, mid)

        # Recursively sort the second half
        self.mergeSortHelper(nums, mid + 1, high)

        # Merge the two sorted halves
        self.merge(nums, low, mid, high)

    def mergeSort(self, nums):
        # Call the helper function to sort the entire list
        self.mergeSortHelper(nums, 0, (len(nums) - 1))
        # Return the sorted list
        return nums

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))

    print(sol.mergeSort(nums))