class Solution:
    def printX(self, X, N):
        if N < 0:
            print("Invalid number of times")
            return
        
        for i in range(N):
            print(X, end='')

            if i < N - 1:
                print(" ", end='')
        
        print()

if __name__ == "__main__":
    sol = Solution()
    X, N = int(input()), int(input())

    sol.printX(X, N)