class Solution:
    def pattern13(self, n):
        number = 1

        for i in range(1, (n + 1)):
            for j in range(1, (i + 1)):
                print(number, end='')
                print(' ', end='')
                number += 1
            
            print()

if __name__ == "__main__":
    sol = Solution()
    n = int(input())

    sol.pattern13(n)