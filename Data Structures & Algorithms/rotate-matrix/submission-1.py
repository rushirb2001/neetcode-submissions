class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # n = len(matrix)
        # rotated = [[0] * n for _ in range(n)]

        # for i in range(n):
        #     for j in range(n):
        #         rotated[j][n - 1 - i] = matrix[i][j]

        # for i in range(n):
        #     for j in range(n):
        #         matrix [i][j] = rotated[i][j]

        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                topLeft = matrix[top][l + i]

                matrix[top][l + i] = matrix[bottom - i][l]

                matrix[bottom - i][l] = matrix[bottom][r - i]

                matrix[bottom][r - i] = matrix[top + i][r]

                matrix[top + i][r] = topLeft

            l += 1
            r -= 1