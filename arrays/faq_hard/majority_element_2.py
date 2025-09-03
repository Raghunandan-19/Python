class Solution:
    def majorityElementTwo(self, nums):
        # Initialize variables for the two potential majority elements and their counts
        n = len(nums)
        ans = []
        el1, el2 = -1, -1
        cnt1, cnt2 = 0, 0

        # First pass: Find candidates for majority elements (> n/3 times)
        for i in range(n):
            if (cnt1 == 0) and (nums[i] != el2):
                el1 = nums[i]
                cnt1 = 1
            elif (cnt2 == 0) and (nums[i] != el1):
                el2 = nums[i]
                cnt2 = 1
            elif nums[i] == el1:
                cnt1 += 1
            elif nums[i] == el2:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        # Second pass: Verify the candidates' actual counts
        cnt1 = 0
        cnt2 = 0

        for i in range(n):
            if nums[i] == el1:
                cnt1 += 1
            elif nums[i] == el2:
                cnt2 += 1

        # Add candidates to the answer list if they appear more than n/3 times
        if cnt1 > (n / 3):
            ans.append(el1)
        
        if cnt2 > (n / 3):
            ans.append(el2)

        return ans

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))

    print(sol.majorityElementTwo(nums))