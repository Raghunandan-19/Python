class Solution:
    #Function to find the median of two sorted arrays.
    def median(self, arr1, arr2):
        # Size of two given arrays
        n1, n2 = len(arr1), len(arr2)

        """ Ensure arr1 is not larger than 
        arr2 to simplify implementation"""
        if n1 > n2:
            return self.median(arr2, arr1)

        n = n1 + n2
        # Length of left half
        left = (n1 + n2 + 1) // 2 

        # Apply binary search
        low, high = 0, n1

        while low <= high:
            # Calculate mid index for arr1
            mid1 = (low + high) // 2 
            
            # Calculate mid index for arr2
            mid2 = left - mid1 

            # Calculate l1, l2, r1, and r2
            l1 = arr1[mid1 - 1] if mid1 > 0 else float('-inf')
            r1 = arr1[mid1] if mid1 < n1 else float('inf')
            l2 = arr2[mid2 - 1] if mid2 > 0 else float('-inf')
            r2 = arr2[mid2] if mid2 < n2 else float('inf')

            if l1 <= r2 and l2 <= r1:
                # If condition for finding median is satisfied
                if n % 2 == 1:
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
            elif l1 > r2:
                # Eliminate the right half of arr1
                high = mid1 - 1
            else:
                # Eliminate the left half of arr1
                low = mid1 + 1
        
        # Dummy statement
        return 0
    
if __name__ == "__main__":
    sol = Solution()
    n1, n2 = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    print(sol.median(arr1, arr2))