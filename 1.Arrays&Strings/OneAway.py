def isOneAway(str1, str2):
    if(len(str1)==len(str2)):
        return isOneReplace(str1, str2)
    
    if(len(str1)+1 == len(str2)):
        return isOneInsert(str1, str2)
    else:
        return isOneInsert(str2, str1)

def isOneReplace(str1, str2):
    replaceCount = 0
    for i in range(len(str1)):
        if str1[i]!=str2[i]:
            replaceCount+=1
        if replaceCount>1:
            return False
    return True

def isOneInsert(str1, str2):
    index1=0
    index2=0

    while index1<len(str1) and index2<len(str2):
        if str1[index1]!=str2[index2]:
            if index1!=index2:
                return False
            else:
                index2+=1
        else:
            index1+=1
            index2+=1
    
    return True

if __name__ == "__main__":
    print(isOneAway("pale","ple"))
    print(isOneAway("pales","pale"))
    print(isOneAway("pale","bale"))