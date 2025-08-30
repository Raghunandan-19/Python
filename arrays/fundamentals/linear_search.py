class Solution:
    def linearSearch(self, nums, target):
        n = len(nums)  # Get the length of the list

        # Iterate through the list to find the target
        for i in range(n):
            if nums[i] == target:  # If the current element matches the target
                return i  # Return the index of the target
        
        return -1  # Return -1 if the target is not found

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))
    target = int(input())

    print(sol.linearSearch(nums, target))