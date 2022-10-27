def nextPermutation(p, n):
    # Write your code here.
    # Return a list.
    marked =-1
    if n==2:
        if(p[0]<p[1]):
            p[1],p[0]=p[0],p[1]
            return p
        else:
            return sorted(p)
    for i in range(n-1,0,-1):
        if(p[i-1]<p[i]):
            marked = i-1
            break
    if marked==-1:
        return sorted(p)
    for j in range(n-1,marked,-1):
        if(p[marked]<p[j]):
            p[marked],p[j]=p[j],p[marked]
            break
    p[marked+1:] = sorted(p[marked+1:])
    return p
    
    pass
