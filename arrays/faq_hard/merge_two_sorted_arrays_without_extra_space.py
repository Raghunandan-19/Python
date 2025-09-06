class Solution:
    def swapIfGreater(self, nums1, nums2, idx1, idx2):
        if nums1[idx1] > nums2[idx2]:
            nums1[idx1], nums2[idx2] = nums2[idx2], nums1[idx1]

    def merge(self, nums1, m, nums2, n):
        len = n + m
        gap = (len // 2) + (len % 2)

        while gap > 0:
            left = 0
            right = left + gap

            while right < len:
                if (left < m) and (right >= m):
                    self.swapIfGreater(nums1, nums2, left, right - m)
                elif left >= m:
                    self.swapIfGreater(nums2, nums2, left - m, right - m)
                else:
                    self.swapIfGreater(nums1, nums1, left, right)
                
                left += 1
                right += 1
            
            if gap == 1:
                break
            
            gap = (gap // 2) + (gap % 2)
        
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