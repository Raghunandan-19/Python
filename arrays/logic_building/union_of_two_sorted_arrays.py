class Solution:
    def unionArray(self, nums1, nums2):
        # Initialize the result array
        union_array = []
        n1 = len(nums1)
        n2 = len(nums2)
        i = 0
        j = 0

        # Traverse both arrays simultaneously
        while (i < n1) and (j < n2):
            if nums1[i] <= nums2[j]:
                # Add nums1[i] if it's not a duplicate
                if (not union_array) or (union_array[-1] != nums1[i]):
                    union_array.append(nums1[i])
                i += 1
            else:
                # Add nums2[j] if it's not a duplicate
                if (not union_array) or (union_array[-1] != nums2[j]):
                    union_array.append(nums2[j])
                j += 1
        
        # Add remaining elements from nums1
        while i < n1:
            if (not union_array) or (union_array[-1] != nums1[i]):
                union_array.append(nums1[i])
                i += 1

        # Add remaining elements from nums2
        while j < n2:
            if (not union_array) or (union_array[-1] != nums2[j]):
                union_array.append(nums2[j])
                j += 1
        
        return union_array

if __name__ == "__main__":
    sol = Solution()
    n1, n2 = map(int, input().split())
    nums1 = list(map(int, input().split()))
    nums2 = list(map(int, input().split()))

    print(sol.unionArray(nums1, nums2))