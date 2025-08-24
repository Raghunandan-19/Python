class Solution:
    def pattern22(self, n):
        for i in range(0, 2 * n - 1):
            for j in range(0, 2 * n - 1):
                top = i
                left = j
                bottom = (2 * n - 2) - i
                right = (2 * n - 2) - j

                print(n - min(min(top, bottom), min(left, right)), end=' ')
            
            print()

if __name__ == "__main__":
    sol = Solution()
    n = int(input())

    sol.pattern22(n)