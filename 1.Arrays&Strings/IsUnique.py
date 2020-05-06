def is_unique(str):
    is_present = [False]*26

    for c in str:
        if is_present[ord(c)-97]:
            return False
        else:
            is_present[ord(c)-97]=True
    
    return True

if __name__ == "__main__":
    print(is_unique("abcdef"))#True
    print(is_unique("ttxder"))#False    