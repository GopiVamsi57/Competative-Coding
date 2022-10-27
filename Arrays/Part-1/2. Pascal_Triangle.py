def printPascal(n:int):
    # Write your code here.
    # Return a list of lists.
    arr=[[1]]
    if n==1:
        return arr
    arr.append([1,1])
    if n==2:
        return arr
    for i in range(2, n):
        prev=[0]*(i+1)
        prev[0]=1
        prev[-1]=1
        for j in range(1, i):
            prev[j]=(arr[-1][j-1]%100000000000007+arr[-1][j]%100000000000007)%100000000000007
        arr.append(prev)
    return arr
    pass
