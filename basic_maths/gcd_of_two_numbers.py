class Solution:
    def GCD(self, n1, n2):
        # Continue looping until one of the numbers becomes zero
        while (n1 > 0) and (n2 > 0):
            if n1 > n2:
                # Replace n1 with the remainder of n1 divided by n2
                n1 %= n2
            else:
                # Replace n2 with the remainder of n2 divided by n1
                n2 %= n1
        
        # When one number becomes zero, return the other as the GCD
        return n1 if n2 == 0 else n2

if __name__ == "__main__":
    sol = Solution()
    n1, n2 = int(input()), int(input())

    print(sol.GCD(n1, n2))