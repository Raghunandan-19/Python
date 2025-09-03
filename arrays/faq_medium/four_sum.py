class Solution:
    def fourSum(self, nums, target):
        n = len(nums)
        ans = []
        nums.sort()  # Sort the array to make it easier to avoid duplicates and use two pointers

        for i in range(n):
            # Skip duplicate values for the first number
            if (i > 0) and (nums[i] == nums[i - 1]):
                continue
            
            for j in range(i + 1, n):
                # Skip duplicate values for the second number
                if (j > i + 1) and (nums[j] == nums[j - 1]):
                    continue
                
                k = j + 1  # Third pointer
                l = n - 1  # Fourth pointer

                while k < l:
                    sum = nums[i] + nums[j] + nums[k] + nums[l]

                    if sum < target:
                        k += 1  # Move left pointer to increase sum
                    elif sum > target:
                        l -= 1  # Move right pointer to decrease sum
                    else:
                        # Found a quadruplet
                        temp = [nums[i], nums[j], nums[k], nums[l]]
                        ans.append(temp)
                        
                        k += 1
                        l -= 1

                        # Skip duplicate values for the third number
                        while (k < l) and (nums[k] == nums[k - 1]):
                            k += 1
                        
                        # Skip duplicate values for the fourth number
                        while (k < l) and (nums[l] == nums[l + 1]):
                            l -= 1
            
        return ans  # Return all unique quadruplets

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))
    target = int(input())

    ans = sol.fourSum(nums, target)

    for row in ans:
        print(row)