class Solution:
    def swapIfGreater(self, nums1, nums2, idx1, idx2):
        # If the element in nums1 at idx1 is greater than the element in nums2 at idx2, swap them
        if nums1[idx1] > nums2[idx2]:
            nums1[idx1], nums2[idx2] = nums2[idx2], nums1[idx1]

    def merge(self, nums1, m, nums2, n):
        # Calculate total length and initial gap for Shell sort-like approach
        length = n + m
        gap = (length // 2) + (length % 2)

        # Continue until gap reduces to 0
        while gap > 0:
            left = 0
            right = left + gap

            # Compare and swap elements with gap distance
            while right < length:
                # Case 1: left in nums1, right in nums2
                if (left < m) and (right >= m):
                    self.swapIfGreater(nums1, nums2, left, right - m)
                # Case 2: both in nums2
                elif left >= m:
                    self.swapIfGreater(nums2, nums2, left - m, right - m)
                # Case 3: both in nums1
                else:
                    self.swapIfGreater(nums1, nums1, left, right)
            
            left += 1
            right += 1
            
            # If gap is 1, next gap will be 0, so break
            if gap == 1:
                break
            
            # Reduce the gap for next iteration
            gap = (gap // 2) + (gap % 2)
        
        # Copy merged elements from nums2 to nums1
        for i in range(m, m + n):
            nums1[i] = nums2[i - m]

if __name__ == "__main__":
    sol = Solution()
    m, n = map(int, input().split())
    nums1 = list(map(int, input().split()))
    nums2 = list(map(int, input().split()))

    nums1 += [0] * (n - (len(nums1) - m))

    sol.merge(nums1, m, nums2, n)
    print(nums1)