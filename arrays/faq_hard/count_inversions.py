class Solution:
    def merge(self, nums, low, mid, high):
        # Temporary list to store merged elements
        merge_list = []
        cnt = 0  # Count of inversions
        left = low  # Pointer for left subarray
        right = mid + 1  # Pointer for right subarray

        # Merge the two sorted subarrays and count inversions
        while (left <= mid) and (right <= high):
            if nums[left] <= nums[right]:
                # No inversion, add left element
                merge_list.append(nums[left])
                left += 1
            else:
                # Inversion found, add right element
                merge_list.append(nums[right])
                cnt += (mid - left + 1)  # Count all remaining elements in left subarray
                right += 1
        
        # Add remaining elements from left subarray
        while left <= mid:
            merge_list.append(nums[left])
            left += 1
        
        # Add remaining elements from right subarray
        while right <= high:
            merge_list.append(nums[right])
            right += 1
        
        # Copy merged elements back to original array
        for i in range(low, high + 1):
            nums[i] = merge_list[i - low]
        
        return cnt  # Return inversion count for this merge
    
    def mergeSort(self, nums, low, high):
        cnt = 0  # Initialize inversion count

        # Base case: If the subarray has one or no elements, no inversions
        if low >= high:
            return cnt
        
        # Find the middle index to divide the array
        mid = low + (high - low) // 2

        # Recursively count inversions in left subarray
        cnt += self.mergeSort(nums, low, mid)

        # Recursively count inversions in right subarray
        cnt += self.mergeSort(nums, mid + 1, high)

        # Count inversions during merge step
        cnt += self.merge(nums, low, mid, high)

        return cnt  # Return total inversion count for this segment

    def numberOfInversions(self, nums):
        # Call mergeSort on the entire array to count inversions
        # Start from index 0 to len(nums) - 1
        return self.mergeSort(nums, 0, len(nums) - 1)
    
if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))

    print(sol.numberOfInversions(nums))