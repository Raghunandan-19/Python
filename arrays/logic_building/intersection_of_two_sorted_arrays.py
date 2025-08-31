class Solution:
    def intersectionArray(self, nums1, nums2):
        # Initialize the result list to store the intersection
        intersection = []
        n1, n2 = len(nums1), len(nums2)
        i, j = 0, 0  # Pointers for nums1 and nums2

        # Traverse both arrays using two pointers
        while (i < n1) and (j < n2):
            if nums1[i] < nums2[j]:
                # Move pointer i if current element in nums1 is smaller
                i += 1
            elif nums1[i] > nums2[j]:
                # Move pointer j if current element in nums2 is smaller
                j += 1
            else:
                # Elements are equal, add to intersection and move both pointers
                intersection.append(nums1[i])
                i += 1
                j += 1
        
        # Return the intersection list
        return intersection

if __name__ == "__main__":
    sol = Solution()
    n1, n2 = map(int, input().split())
    nums1 = list(map(int, input().split()))
    nums2 = list(map(int, input().split()))

    print(sol.intersectionArray(nums1, nums2))