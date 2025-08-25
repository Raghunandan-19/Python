class Solution:
    def secondMostFrequentElement(self, nums):
        n = len(nums)
        mpp = {}  # Dictionary to store frequency of each element

        highest_ele = -1
        highest_freq = 0
        second_highest_ele = -1
        second_highest_freq = 0

        # Count frequency of each element
        for num in nums:
            if num in mpp:
                mpp[num] += 1
            else:
                mpp[num] = 1
        
        # Find the element with highest and second highest frequency
        for ele, freq in mpp.items():
            if freq > highest_freq:
                # Update second highest before updating highest
                second_highest_ele = highest_ele
                highest_ele = ele
                second_highest_freq = highest_freq
                highest_freq = freq
            elif freq == highest_freq:
                # If tie for highest frequency, choose smaller element
                highest_ele = min(highest_ele, ele)
            elif freq > second_highest_freq:
                # Update second highest if current freq is greater
                second_highest_freq = freq
                second_highest_ele = ele
            elif freq == second_highest_freq:
                # If tie for second highest, choose smaller element
                second_highest_ele = min(second_highest_ele, ele)
        
        return second_highest_ele
                
if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))

    print(sol.secondMostFrequentElement(nums))