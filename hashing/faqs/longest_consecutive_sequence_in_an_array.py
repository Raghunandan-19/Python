class Solution:
    def longestConsecutive(self, nums):
        st = set()  # Create a set to store unique elements

        n = len(nums)
        if n == 0:
            return 0  # If the list is empty, return 0
        
        longest_sequence = 1  # Initialize the longest sequence length

        # Add all elements to the set for O(1) lookups
        for i in range(n):
            st.add(nums[i])
        
        # Iterate through each unique element in the set
        for it in st:
            # Check if 'it' is the start of a sequence
            if (it - 1) not in st:
                count_current = 1  # Start counting the current sequence
                num = it

            # Count consecutive numbers in the sequence
            while (num + 1) in st:
                num += 1
                count_current += 1
            
            # Update the longest sequence found so far
            longest_sequence = max(longest_sequence, count_current)
        
        return longest_sequence  # Return the length of the longest consecutive sequence

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))

    print(sol.longestConsecutive(nums))