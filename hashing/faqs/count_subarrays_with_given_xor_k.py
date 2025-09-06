class Solution:
    def subarraysWithXorK(self, nums, k):
        n = len(nums)
        mpp = {0 : 1}  # Dictionary to store prefix XOR frequencies

        prefix_xor = 0  # Initialize prefix XOR
        count = 0       # Initialize count of subarrays

        for i in range(n):
            prefix_xor ^= nums[i]  # Update prefix XOR with current element
            xor_to_remove = prefix_xor ^ k  # Find the required prefix XOR to get XOR=k
            count += mpp.get(xor_to_remove, 0)  # Add the number of times this XOR has occurred
            mpp[prefix_xor] = mpp.get(prefix_xor, 0) + 1  # Update the frequency of current prefix XOR
        
        return count  # Return the total count of subarrays

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))

    k = int(input())

    print(sol.subarraysWithXorK(nums, k))