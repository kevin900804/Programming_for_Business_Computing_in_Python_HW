getData = input()
data = getData.split(",")
demandFree = int(data[0]) # 此商品免費時的需求量
saleAdd = float(data[1]) # 對方商品漲 1 元時會增加的銷售量
cost1 = int(data[2]) # 零售商 1 的商品成本
cost2 = int(data[3]) # 零售商 2 的商品成本
iterationNum = int(data[4]) # 雙方共互動 n 輪

r1_decisionList = []
r2_decisionList = []
r1_begin = (demandFree + cost1) / 2 # 零售商 1 第 0 輪決策
r2_begin = (demandFree + saleAdd * r1_begin + cost2) / 2 # 零售商 2 第 0 輪決策
r1_decisionList.append(r1_begin)
r2_decisionList.append(r2_begin)

for i in range(iterationNum): # 零售商 2 根據零售商 1 的決策行動，共進行 n 輪
    r1_decision = (demandFree + saleAdd * r2_decisionList[-1] + cost1) / 2
    r1_decisionList.append(r1_decision)
    r2_decision = (demandFree + saleAdd * r1_decisionList[-1] + cost2) / 2
    r2_decisionList.append(r2_decision)

Eq1 = r1_decisionList[-1]
Eq2 = r2_decisionList[-1]
print("%0.2f %0.2f" % (Eq1, Eq2)) # 最後的equilibrium情形