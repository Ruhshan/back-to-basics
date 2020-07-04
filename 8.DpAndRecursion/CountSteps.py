def countSteps(n):
    if n==1 or n==0:
        return 1
    elif n==2:
        return 2
    else:
        return countSteps(n-3)+countSteps(n-2)+countSteps(n-1)

if __name__ == "__main__":
    print(countSteps(5))