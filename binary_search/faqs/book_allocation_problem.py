class Solution:
    def countStudents(self, nums, pages):
        n = len(nums)
        students = 1  # Start with one student
        pages_student = 0  # Pages allocated to current student

        for i in range(n):
            # If adding this book doesn't exceed the limit, allocate to current student
            if (pages_student + nums[i]) <= pages:
                pages_student += nums[i]
            else:
            # Otherwise, allocate to next student
                students += 1
                pages_student = nums[i]  # Start counting pages for new student
        
        return students  # Return total students needed for this allocation
    
    def findPages(self, nums, m):
        n = len(nums)

        # If number of students is more than number of books, allocation is not possible
        if m > n:
            return -1
        
        # Initialize search boundaries
        low = -float("inf")  # Minimum possible value (max of nums)
        high = 0             # Maximum possible value (sum of nums)

        # Find the minimum and maximum possible values for binary search
        for i in range(n):
            low = max(low, nums[i])  # At least one book per student, so min is the largest book
            high += nums[i]          # Max is sum of all books (one student gets all)
        
        # Binary search to find the minimum maximum pages
        while low <= high:
            mid = low + (high - low) // 2

            # If more students are needed, increase lower bound
            if self.countStudents(nums, mid) > m:
                low = mid + 1
            else:
            # Try for a better (smaller) maximum
                high = mid - 1
        
        return low  # This is the minimum possible maximum pages
    
if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    nums = list(map(int, input().split()))
    m = int(input())

    print(sol.findPages(nums, m))