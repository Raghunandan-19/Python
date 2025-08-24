class Solution:
    def sum(self,arr, n): 
        # Initialize sum_of_elements to store the sum of array elements
        sum_of_elements = 0

        # Iterate through the array up to n elements
        for i in range(n):
            # Add each element to sum_of_elements
            sum_of_elements += arr[i]
        
        # Return the final sum
        return sum_of_elements

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    arr = list(map(int, input().split()))

    print(sol.sum(arr, n))