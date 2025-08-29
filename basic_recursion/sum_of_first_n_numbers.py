class Solution:
    def nNumbersSum(self, N):
        # Base case: if N is less than 1, return 0
        if N < 1:
            return 0
        
        # Recursive case: sum N with the sum of numbers up to N-1
        return N + self.nNumbersSum(N - 1)

if __name__ == "__main__":
    sol = Solution()
    N = int(input())

    print(sol.nNumbersSum(N))