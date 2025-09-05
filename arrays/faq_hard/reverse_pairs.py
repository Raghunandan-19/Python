class Solution:
    def merge(self, nums, low, mid, high):
        # Temporary list to store merged elements
        merge_list = []
        left = low
        right = mid + 1

        # Merge the two sorted halves into merge_list
        while (left <= mid) and (right <= high):
            if nums[left] <= nums[right]:
                merge_list.append(nums[left])
                left += 1
            else:
                merge_list.append(nums[right])
                right += 1
        
        # Copy any remaining elements from the left half
        while left <= mid:
            merge_list.append(nums[left])
            left += 1

        # Copy any remaining elements from the right half
        while right <= high:
            merge_list.append(nums[right])
            right += 1
        
        # Copy the merged elements back into the original array
        for i in range(low, high + 1):
            nums[i] = merge_list[i - low]
    
    def countPairs(self, nums, low, mid, high):
        cnt = 0
        right = mid + 1

        # For each element in the left half, count elements in the right half
        # such that nums[i] > 2 * nums[right]
        for i in range(low, mid + 1):
            while (right <= high) and (nums[i] > (2 * nums[right])):
                right += 1
            # The number of valid pairs for nums[i] is (right - (mid + 1))
            cnt += (right - (mid + 1))
        
        return cnt
    
    def mergeSort(self, nums, low, high):
        cnt = 0

        # Base case: if the subarray has one or no elements, no reverse pairs
        if low >= high:
            return cnt
        
        # Find the middle index
        mid = low + (high - low) // 2

        # Count reverse pairs in the left half
        cnt += self.mergeSort(nums, low, mid)
        # Count reverse pairs in the right half
        cnt += self.mergeSort(nums, mid + 1, high)
        # Count reverse pairs across the two halves
        cnt += self.countPairs(nums, low, mid, high)
        # Merge the two sorted halves
        self.merge(nums, low, mid, high)
        
        return cnt

    def reversePairs(self, nums):
        # Call mergeSort on the entire array to count reverse pairs
        return self.mergeSort(nums, 0, len(nums) - 1)

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))

    print(sol.reversePairs(nums))