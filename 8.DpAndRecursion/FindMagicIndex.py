def magicFirst(array):
    return findMagicIndex(array, 0, len(array)-1)

def findMagicIndex(array, start, end):
    if end < start:
        return -1
    
    midIndex = (start + end)/2
    midValue = array[midIndex]

    if midValue == midIndex:
        return midIndex
    
    #Search Left
    leftIndex = min(midIndex -1, midValue)
    left = findMagicIndex(array, start, leftIndex)

    if left >= 0:
        return left
    
    #Search Right

    rightIndex = max(midIndex + 1, midValue)
    right = findMagicIndex(array, rightIndex, end)

    return right

if __name__ == "__main__":
    array = [-10, -5, 3,2,2,3,4,7,9,12,13]

    print(magicFirst(array))
