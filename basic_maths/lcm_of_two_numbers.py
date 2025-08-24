class Solution:
    def GCD(self, n1, n2):
        # Use the Euclidean algorithm to find the Greatest Common Divisor (GCD)
        while (n1 > 0) and (n2 > 0):
            if n1 > n2:
                n1 %= n2  # Replace n1 with the remainder of n1 divided by n2
            else:
                n2 %= n1  # Replace n2 with the remainder of n2 divided by n1
        
        # When one number becomes zero, the other is the GCD
        return n1 if n2 == 0 else n2
    
    def LCM(self, n1, n2):
        # Calculate and return the Least Common Multiple (LCM)
        # LCM of two numbers is (n1 * n2) divided by their Greatest Common Divisor (GCD)
        return (n1 * n2) // self.GCD(n1, n2)

if __name__ == "__main__":
    sol = Solution()
    n1, n2 = int(input()), int(input())

    print(sol.LCM(n1, n2))