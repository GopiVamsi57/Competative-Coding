def maxSubarraySum(A, n) :
    l,r,max_sum,curr_sum = 0,0,0,0
    for i in range(n):
        curr_sum += A[i]
        if(curr_sum>max_sum):
            max_sum=curr_sum
            r+=1
        elif(curr_sum<0):
            curr_sum=0
            l=i+1 
            r=i+1
        else:
            r+=1
    return max_sum
