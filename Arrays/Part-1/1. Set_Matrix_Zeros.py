def Convert_to_zeros(matrix,R_mark,C_mark,N,M):
    for i in range(N):
        for j in range(M):
            if(R_mark[i]==1 or C_mark[j]==1):
                matrix[i][j]=0
    return matrix
            
def setZeros(matrix: List[List[int]]) -> None:
	# Write your code here.
    N,M = len(matrix),len(matrix[0])
    R_mark,C_mark = [0]*N,[0]*M
    for i in range(N):
       for j in range(M):
        if(matrix[i][j] == 0):
            R_mark[i],C_mark[j] = 1,1
    return Convert_to_zeros(matrix,R_mark,C_mark,N,M)
    pass
