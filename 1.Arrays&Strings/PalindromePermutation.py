def is_palindromic_permutation(str):
    charCount = [0]*26

    oddCount=0

    for c in str:
        if c.isalpha():
            charCount[ord(c)-97]+=1

            if charCount[ord(c)-97]%2==1:
                oddCount+=1
            else:
                oddCount-=1
    
    return oddCount <=1






if __name__ == "__main__":
    print(is_palindromic_permutation("taco catx"))
    