class Solution:
    def pattern12(self, n):
        spaces = 2 * (n - 1)

        for i in range(1, (n + 1)):
            # numbers
            for j in range (1, (i + 1)):
                print(j, end='')
            
            # spaces
            for j in range(1, (spaces + 1)):
                print(' ', end='')

            # numbers
            for j in range(i, 0, -1):
                print(j, end='')
            
            print()

            spaces -= 2

if __name__ == "__main__":
    sol = Solution()
    n = int(input())

    sol.pattern12(n)