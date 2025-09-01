class Solution:
    def generateRow(self, r):
        ans = [0] * r  # Initialize a list of size r with all elements as 0

        ans[0] = 1  # The first element of every row in Pascal's Triangle is always 1

        # Compute each element of the row using the previous element and the formula for binomial coefficients
        for i in range(1, r):
            ans[i] = (ans[i-1] * (r - i)) // i  # Calculate the next element based on the previous one

        return ans  # Return the generated row
        
    def pascalTriangleIII(self, n):
        ans = []  # Initialize a list to store all rows of Pascal's Triangle

        # Loop through each row number from 1 to n
        for i in range(1, n + 1):
            # Generate the i-th row and append it to the answer list
            ans.append(self.generateRow(i))
        
        return ans  # Return the complete Pascal's Triangle up to n rows

if __name__ == "__main__":
    sol = Solution()
    n = int(input())

    ans = sol.pascalTriangleIII(n)

    for row in ans:
        print(row)