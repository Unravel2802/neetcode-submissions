class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Idea:
        # Rotate 90° clockwise = transpose the matrix then reverse each row

        n = len(matrix)

        # transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # reverse each row
        for i in range(n):
            matrix[i].reverse()