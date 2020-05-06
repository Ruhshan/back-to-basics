def urlize(str):
    spaces=0
    characters=0

    for c in str:
        if c == " ":
            spaces+=1
        else:
            characters+=1
    
    newStrLen = characters+(3*spaces)
    urlizedStr = [" "]*(newStrLen)

    index = newStrLen-1

    for i in range(characters+spaces-1,-1,-1):
        if str[i]==" ":
            urlizedStr[index]="0"
            urlizedStr[index-1]="2"
            urlizedStr[index-2]="%"
            index-=3
        else:
            urlizedStr[index] = str[i]
            index-=1
            
    print("".join(urlizedStr))

if __name__ == "__main__":
    print(urlize("Mr. John Smith"))