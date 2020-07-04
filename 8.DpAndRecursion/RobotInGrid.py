def getPath(maze):
    if len(maze) == 0 or len(maze[0]) == 0:
        return None
    path = []
    failedPoints = set()
    if pathFinder(maze, len(maze)-1, len(maze[0])-1, path, failedPoints):
        return path
    return None

def pathFinder(maze, row, col, path, failedPoints):
    if col < 0 or row < 0 or not maze[row][col]:
        return False
    p = (row, col)
    if p in failedPoints:
        return False
    isAtOrigin = (row == 0) and (col == 0)
    if isAtOrigin or pathFinder(maze, row, col-1, path, failedPoints) or pathFinder(maze, row-1, col, path, failedPoints):
        path.append(p)
        return True
    failedPoints.append(p)
    return False

if __name__ == "__main__":
    maze = [[True, True,True,True],
           [True, False, True, True],
            [True, True, False, True],
            [True, True, True, True]]
    
    print(getPath(maze))
    