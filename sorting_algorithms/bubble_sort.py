class Solution:
    def bubbleSort(self, nums):
        n = len(nums)  # Get the length of the list

        # Traverse the list from the end to the start
        for i in range((n - 1), -1, -1):
            did_swap = False  # Track if any swaps are made in this pass

            # Compare adjacent elements and swap if needed
            for j in range(0, i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]  # Swap
                    did_swap = True  # Mark that a swap occurred
                
            # If no swaps were made, the list is sorted
            if did_swap == False:
                break
        
        return nums  # Return the sorted list

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))

    print(sol.bubbleSort(nums))