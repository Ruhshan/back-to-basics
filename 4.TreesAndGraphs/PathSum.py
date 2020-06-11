from binarytree import Node

pathCount = {}
def countPathWithSum(node, targetSum, runningSum):
    global pathCount

    if node == None:
        return 0
    runningSum = runningSum+node.value
    difference = runningSum - targetSum

    totalPaths = pathCount.get(difference, 0)

    print("------")
    print("tp", difference,totalPaths)
    print("node", node.value)
    print("rs",runningSum)
    print("pk", pathCount)

    if runningSum == targetSum:
        totalPaths+=1

    updatePathCount(runningSum,1)
    totalPaths += countPathWithSum(node.left, targetSum, runningSum)
    totalPaths += countPathWithSum(node.right, targetSum, runningSum)
    updatePathCount(runningSum,-1)

    print("pathsum", totalPaths)
    print("*******")

    return totalPaths

def updatePathCount(key, value):
    global pathCount
    newCount = pathCount.get(key, 0) + value

    if newCount == 0:
        del pathCount[key]
    else:
        pathCount[key] = newCount


    

def incrementPathCount(key, delta):
    global pathCount
    newCount = pathCount.get(key, 0) + delta
    if newCount == 0:
        del pathCount[key]
    else:
        pathCount[key] = newCount
    

if __name__ == "__main__":
    node10 = Node(10)
    node5 = Node(5)
    nodeM3 = Node(-3)
    nodeM3.right = Node(11)

    node10.left = node5
    node10.right = nodeM3

    node3 = Node(3)
    node2 = Node(2)

    node5.left = node3
    node5.right = node2

    node2.right = Node(1)

    node32 = Node(3)
    nodeM2 = Node(-2)

    node3.left = node32
    node3.right = nodeM2

    fsum = countPathWithSum(node10, 15, 0)

    print("Final", fsum)



    