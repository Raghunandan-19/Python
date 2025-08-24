class Solution:
    def pattern18(self, n):
        for i in range(n):
            for ch in range(ord('A') + n - 1 - i, ord('A') + n):
                print(chr(ch), end=" ")
    
            print()

if __name__ == "__main__":
    sol = Solution()
    n = int(input())

    sol.pattern18(n)