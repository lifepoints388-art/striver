# Stock Buy And Sell



# Brute Force Approach 
def Stock_sell(prices,n):
    maxprofit=0
    for i in range(n):
        for j in range(i,n):
            profit=prices[j]-prices[i]
            if profit>maxprofit:
                maxprofit=profit
    return maxprofit
prices=[7,1,5,3,6,4]
n=len(prices)
res=Stock_sell(prices,n)
print(res)

# optimal approach
def Stock(prices,n):
    mincost=prices[0]
    maxprofit=0
    for i in range(1,n):
        profit=prices[i]-mincost 
        if profit>maxprofit:
            maxprofit=profit
        if mincost>prices[i]:
            mincost=prices[i]
    return maxprofit
prices=[7,1,5,3,6,4]
n=len(prices)
res=Stock(prices,n)
print(res)