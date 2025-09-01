class Solution:
    def nCr(self, n, r):
        # Initialize result
        res = 1

        # Calculate nCr using iterative method to avoid large factorials
        for i in range(r):
            res *= (n - i)      # Multiply by (n - i)
            res //= (i + 1)     # Divide by (i + 1) to maintain integer division
        
        # Return the computed binomial coefficient
        return res

    def pascalTriangleI(self, r, c):
        # In Pascal's Triangle, the value at row r and column c is given by nCr = (r-1)C(c-1)
        return self.nCr(r - 1, c - 1)

if __name__ == "__main__":
    sol = Solution()
    r = int(input())
    c = int(input())

    print(sol.pascalTriangleI(r, c))