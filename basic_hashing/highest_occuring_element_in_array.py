class Solution:
    def mostFrequentElement(self, nums):
        n = len(nums)  # Get the length of the input list

        max_freq = 0   # To store the highest frequency found so far
        max_ele = 0    # To store the element with the highest frequency

        mpp = {}       # Dictionary to store frequency of each element

        # Count the frequency of each element
        for num in nums:
            if num in mpp:
                mpp[num] += 1
            else:
                mpp[num] = 1

        # Find the element with the highest frequency
        for ele, freq in mpp.items():
            if freq > max_freq:
                max_freq = freq
                max_ele = ele
            elif freq == max_freq:
                # If frequencies are equal, choose the smaller element
                max_ele = min(max_ele, ele)
        
        return max_ele  # Return the most frequent element

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))

    print(sol.mostFrequentElement(nums))