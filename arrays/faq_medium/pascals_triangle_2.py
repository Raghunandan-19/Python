class Solution:
    def pascalTriangleII(self, r):
        # Initialize a list of size r with zeros
        ans = [0] * r  
        
        # The first element of every row in Pascal's Triangle is always 1
        ans[0] = 1 
        
        # Compute each element using the previous element and the formula for binomial coefficients
        for i in range(1, r):
            ans[i] = (ans[i-1] * (r - i)) // i
        
        # Return the computed row as a list
        return ans

if __name__ == "__main__":
    sol = Solution()
    r = int(input())

    print(sol.pascalTriangleII(r))