class Solution:
    def threeSum(self, nums):
        n = len(nums)
        nums.sort()  # Sort the array to use two-pointer technique
        ans = []

        for i in range(n):
            # Skip duplicate values for the first element
            if (i > 0) and (nums[i - 1] == nums[i]):
                continue

            j = i + 1  # Left pointer
            k = n - 1  # Right pointer

            while j < k:
                temp = []
                sum = nums[i] + nums[j] + nums[k]

                if sum == 0:
                    # Found a triplet
                    temp.append(nums[i])
                    temp.append(nums[j])
                    temp.append(nums[k])
                    ans.append(temp)
                    j += 1
                    k -= 1

                    # Skip duplicates for the second element
                    while (j < k) and (nums[j - 1] == nums[j]):
                        j += 1
                    
                    # Skip duplicates for the third element
                    while (j < k) and (nums[k] == nums[k + 1]):
                        k -= 1
                elif sum < 0:
                    # Need a larger sum, move left pointer to the right
                    j += 1
                else:
                    # Need a smaller sum, move right pointer to the left
                    k -= 1
        
        return ans

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))

    print(sol.threeSum(nums))