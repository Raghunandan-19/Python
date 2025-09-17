class Solution:
    def kthElement(self, a, b, k):
        m = len(a)
        n = len(b)

        # Ensure a is smaller array for optimization
        if m > n:
            # Swap a and b
            return self.kthElement(b, a, k)
        
        # Length of the left half
        left = k

        # Apply binary search
        low = max(0, k - n)
        high = min(k, m)
        while low <= high:
            mid1 = (low + high) >> 1
            mid2 = left - mid1

            # Initialize l1, l2, r1, r2
            l1 = a[mid1 - 1] if mid1 > 0 else float('-inf')
            l2 = b[mid2 - 1] if mid2 > 0 else float('-inf')
            r1 = a[mid1] if mid1 < m else float('inf')
            r2 = b[mid2] if mid2 < n else float('inf')

            # Check if we have found the answer
            if l1 <= r2 and l2 <= r1:
                return max(l1, l2)
            elif l1 > r2:
                # Eliminate the right half
                high = mid1 - 1
            else:
                # Eliminate the left half
                low = mid1 + 1
        
        # Dummy return statement
        return -1
    
if __name__ == "__main__":
    sol = Solution()
    n1, n2 = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    k = int(input())

    print(sol.kthElement(a, b, k))