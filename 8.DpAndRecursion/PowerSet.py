
def powerSet(elements):
    if len(elements)==0:
        return ""
    else:
        ps = powerSet(elements[0:len(elements)-1])
        return add(ps, elements[-1])

def add(oldSet, newElement):
    if oldSet == "":
        return ["",newElement]
    newSet = oldSet.copy()
    for e in oldSet:
        newSet.append(e+newElement)
    
    return newSet


if __name__ == "__main__":
    print(powerSet(["a","b","c"]))