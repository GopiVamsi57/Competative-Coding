def maximumProfit(prices):
    # Write your code here.
    min_so_far=prices[0]
    profit=0
    max_profit=0
    for i in range(1,len(prices)):
        if prices[i]<min_so_far:
            min_so_far = prices[i]
        else:
            profit =  prices[i]-min_so_far
            if profit>max_profit:
                max_profit=profit
    return max_profit
