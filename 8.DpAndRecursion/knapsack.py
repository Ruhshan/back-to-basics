def knapSack(capacity, wt, prof):
    n = len(prof)
    table = [[0 for x in range(capacity + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for j in range(capacity + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif wt[i - 1] <= j:
                table[i][j] = max(prof[i - 1]+ table[i - 1][j - wt[i - 1]], table[i - 1][j])
            else:
                table[i][j] = table[i - 1][j]





    return table[n][capacity], find_included_items(table, weights, capacity)

def find_included_items(table, weights, capacity):
    items = []

    for i in range(len(weights),0,-1):
        if table[i][capacity]!= table[i-1][capacity]:
            items.append(weights[i-1])
            capacity-=weights[i-1]

    return items





if __name__=="__main__":
    weights = [0,1,2,3,4]
    profits = [2,7,9,3,1]
    capacity = 100
    print(knapSack(capacity, weights, profits))