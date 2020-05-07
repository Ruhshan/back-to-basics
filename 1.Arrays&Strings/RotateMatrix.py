def rotateMatrix(matrix, n):
    for i in range(n/2):
        for j in range(i, n-i-1):
            tempTop = matrix[i][j]
            tempLeft = matrix[n-1-j][i]
            tempBottom = matrix[n-1][n-1-j]
            tempRight = matrix[j][n-1-i]
            
            matrix[n-1-j][i]= tempTop#top goes left
            matrix[n-1][n-1-j] = tempLeft # left goes bottom
            matrix[j][n-1-i] = tempBottom #bottom goes right
            matrix[i][j] = tempRight #right goes top

    for l in matrix:
        print l    
if __name__ == "__main__":
    m = [
            [1,2,3,"a"],
            [4,5,6,"b"],
            [7,8,9,"c"],
            [10,11,12,"d"]
        ]
    rotateMatrix(m, 4) 