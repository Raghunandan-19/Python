class Solution:
    def rotateMatrix(self, matrix):
        n = len(matrix)  # Get the size of the matrix (assuming it's square)

        # Transpose the matrix (swap rows and columns)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse each row to get the rotated matrix
        for i in range(n):
            matrix[i].reverse()

if __name__ == "__main__":
    sol = Solution()
    n, m = map(int, input().split())
    matrix = []

    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    sol.rotateMatrix(matrix)

    for row in matrix:
        print(row)