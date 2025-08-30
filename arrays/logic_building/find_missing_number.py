class Solution:
    def missingNumber(self, nums):
        xor1 = 0  # XOR of all elements in the array
        xor2 = 0  # XOR of all numbers from 1 to n

        # XOR all elements in nums and all indices + 1 (which gives numbers from 1 to n)
        for i in range(len(nums)):
            xor1 ^= nums[i]
            xor2 ^= (i + 1)
        
        # The missing number is the XOR of xor1 and xor2
        return (xor1 ^ xor2)
    
if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))

    print(sol.missingNumber(nums))