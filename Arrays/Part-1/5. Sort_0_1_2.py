def sort012( n) :
    global arr
    dict = {0:0,1:0,2:0}
    for x in arr:
        dict[x]+=1
    arr = [0]*dict[0]+[1]*dict[1]+[2]*dict[2]
    pass
