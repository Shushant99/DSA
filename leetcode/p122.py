prices=[7,1,5,3,6,4]
sum=0
buy=0

for sell in range(buy+1,len(prices)):
    if prices[buy]<prices[sell]:
        sum+=prices[sell]-prices[buy]
        buy=sell
        
    else:
        buy+=1
print(sum)