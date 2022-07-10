import pandas as pd

def readData():
    stockData = pd.DataFrame(pd.read_csv("prices-split-adjusted.csv")) 
    stockData["profit"]= None
    stockData = stockData[["date", "symbol", "close","profit"]]
    return stockData

def stockDetails(stock):
    data = readData()
    TheStock = data[data["symbol"]==stock]
    profit= [0]*len(TheStock["profit"])

    for i in range(1, len(profit)):
        profit[i] = TheStock["close"].iloc[i] - TheStock["close"].iloc[i-1]

    
    maxProfit = MSSDAC(profit)
    return f"Max Profit: ${maxProfit[0]:.2f}, Buy on: {TheStock['date'].iloc[maxProfit[1]]}, Sell on: {TheStock['date'].iloc[maxProfit[2]]}"

def getCompanyProfit():
    companies = pd.DataFrame(pd.read_csv("securities.csv"))
    companies = companies[["Ticker symbol", "Security"]]
    pricesData = readData()
    bestProfit = 0

    for tick in companies["Ticker symbol"]:
        
        if tick in pricesData["symbol"].values:
            currentTick = stockDetails(tick)
            currentProfit = currentTick[0]
            
            if currentProfit > bestProfit:
                bestProfit = currentProfit
                
                bestStock = companies["Security"].iloc[companies["Ticker symbol"][companies["Ticker symbol"] == tick].index.tolist()[0]]
                bestBuy = currentTick[1]
                bestSell = currentTick[2]
    
    return f"Best Stock to buy: \"{bestStock}\" on {bestBuy} and \n sell on {bestSell} with profit of {bestProfit}"


def MSSDAC(A, low= 0, high= None):
    right = left = None
    
    if high == None:
        high = len(A)-1
    
    # base case
    if low == high:
        if A[low] > 0:
            return A[low], low
        else:
            return 0, None
    
    # divide
    mid = (low+high)//2

    # conquer
    maxLeft= MSSDAC(A, low, mid)
    maxRight= MSSDAC(A, mid+1, high)

    # left max initiation
    maxLeft2Center = left2Center = 0

    # calc left of center max
    for i in range(mid, low-1, -1):
        left2Center  += A[i]
        if maxLeft2Center < max(maxLeft2Center, left2Center):
            maxLeft2Center = max(maxLeft2Center, left2Center)
            left = i-1
            
    # right max initiation
    maxRight2Center = right2Center = 0

    # calc rigt of center max
    for i in range(mid+1, high+1):
        right2Center += A[i]
        if maxRight2Center < max(maxRight2Center, right2Center):
            maxRight2Center = max(maxRight2Center, right2Center)
            right = i-1
            
    maxProfit = max(maxLeft[0], maxRight[0], maxLeft2Center+maxRight2Center)
    
    if maxProfit == maxLeft[0]:
        return maxLeft

    elif maxProfit == maxRight[0]:
        return maxRight

    else:
        return maxLeft2Center+maxRight2Center, left, right 

if __name__ =="__main__":
    print(stockDetails('AAPL'))