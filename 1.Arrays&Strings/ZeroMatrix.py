def zeroMatrix(matrix):
    cols = len(matrix[0])
    rows = len(matrix)

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0

    
    for col in range(cols):
        if matrix[0][col]== 0:
            for row in range(rows):
                matrix[row][col]=0

    for row in range(rows):
        if matrix[row][0]  == 0:
            for col in range(cols):
                matrix[row][col]=0

    for l in matrix:
        print l

if __name__ == "__main__":
    m = [
            [1,2,3,12],
            [4,0,6,0],
            [7,8,9,12]
        ]
    zeroMatrix(m)