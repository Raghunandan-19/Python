class Solution:
    def singleNonDuplicate(self, nums):
        n = len(nums)
        
        # If there's only one element, return it
        if n == 1:
            return nums[0]
        
        # Check if the first element is the single one
        if nums[0] != nums[1]:
            return nums[0]
        
        # Check if the last element is the single one
        if nums[-2] != nums[-1]:
            return nums[-1]

        low = 1
        high = n - 2

        # Binary search for the single element
        while low <= high:
            mid = low + (high - low) // 2

            # If mid is the single element
            if (nums[mid - 1] != nums[mid]) and (nums[mid] != nums[mid + 1]):
                return nums[mid]

            # Decide which half to search next
            # If mid is odd and equals previous, or mid is even and equals next, move right
            if (((mid % 2) == 1) and (nums[mid - 1] == nums[mid])) or ((mid % 2 == 0) and (nums[mid] == nums[mid + 1])):
                low = mid + 1
            else:
                high = mid - 1

        # If not found, return -1 (should not happen for valid input)
        return -1

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))

    print(sol.singleNonDuplicate(nums))