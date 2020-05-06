
def check_permutation(str1, str2):
    counts=[0]*26

    for c in str1:
        counts[ord(c)-97]+=1
    
    for c in str2:
        counts[ord(c)-97]-=1

        if counts[ord(c)-97]==-1:
            return False
    
    return True


if __name__ == "__main__":
    print(check_permutation("abcc", "cxbc"))#True