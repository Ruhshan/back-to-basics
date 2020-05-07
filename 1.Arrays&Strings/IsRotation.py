def isRotation(str1, str2):
    return str2 in str1+str1
if __name__ == "__main__":
    print(isRotation("waterbottle","erbottlewat"))