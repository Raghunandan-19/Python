class Solution:
    def majorityElement(self, nums):
        n = len(nums)
        el = -1  # Candidate for majority element
        cnt = 0  # Counter for current candidate

        # First pass: Find a candidate for majority element using Boyer-Moore Voting Algorithm
        for i in range(n):
            if cnt == 0:
                el = nums[i]  # Set new candidate
                cnt = 1
            elif el == nums[i]:
                cnt += 1  # Increment count if same as candidate
            else:
                cnt -= 1  # Decrement count if different

        cnt = 0  # Reset counter for verification

        # Second pass: Verify if candidate is actually the majority element
        for i in range(n):
            if nums[i] == el:
                cnt += 1

        # Check if candidate occurs more than n/2 times
        if cnt > (n / 2):
            return el

        return -1  # No majority element found

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))

    print(sol.majorityElement(nums))