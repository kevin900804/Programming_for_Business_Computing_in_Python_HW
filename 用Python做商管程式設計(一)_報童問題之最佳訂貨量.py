while True:
    cost = int(input()) # 單位進貨成本 c
    price = int(input()) # 單位零售價格 r
    maxNeed = int(input()) # 需求的可能個數 N

    bestProfit = 0
    bestOrder = 0

    probs = []
    for i in range(maxNeed + 1):
        probs.append(float(input())) # 將機率輸入
    print(probs)

    for order in range(maxNeed + 1):
        expSales = 0 # 期望值歸0，避免影響下一run
        for demand in range(maxNeed + 1): # 0,1,2,3,4,5,6,7,8
            prob = probs[demand] # 取出機率
            if order > demand:
                expSales += prob * demand
            else:
                expSales += prob * order
        profit = price * expSales - cost * order # 計算利潤

        if profit > bestProfit:
            bestProfit = profit
            bestOrder = order

    print(bestOrder,int(bestProfit))