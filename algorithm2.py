def maxProfit(prices):
    minimum=prices[0]
    maximum=0
    
    for i in range(1,len(prices)):
        if prices[i] < minimum:
            minimum=prices[i]
        elif prices[i]>maximum :
            maximum=prices[i]
   
    if (maximum-minimum) <= 0:
        return 0
    return maximum-minimum 



print("Result Test 1: ", maxProfit([7, 1, 5, 3, 6, 4]))

print("Result Test 2 : ", maxProfit([7, 6, 4,3,2,1]))