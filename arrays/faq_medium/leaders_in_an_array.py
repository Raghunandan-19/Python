class Solution:
    def leaders(self, nums):
        n = len(nums)
        leader = []
        # The rightmost element is always a leader
        current_leader = nums[-1]
        leader.append(nums[-1])

        # Traverse the array from right to left
        for i in range(n - 2, -1, -1):
            # If the current element is greater than the current leader,
            # it is a new leader
            if nums[i] > current_leader:
                current_leader = nums[i]
                leader.append(nums[i])
        
        # Reverse to maintain the order as in the original array
        leader.reverse()

        return leader

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))

    print(sol.leaders(nums))