import numpy as np

dataGet = input() # 輸入 n p d
data = dataGet.split() # 存放n p d，n=城鎮總數、p=欲設置基地台的城鎮數 、d=基地台覆蓋公里數
towns = int(data[0])
totalSet = int(data[1])
coverDistance = int(data[2])
populationSum = 0
    
statusData = []
for town in range(towns):
    statusGet = input() # 存放x座標、y座標、人口數
    status = statusGet.split()
    statusInt = []
    for i in status:
        statusInt.append(int(i)) # 將字串轉換為整數
    statusData.append(statusInt) # 將各城鎮資料存進清單
    
distanceData = []
population = []
for i in statusData:
    population.append(i[2]) # 取出所有人口的資料
    for j in statusData:
        x_distance = (i[0] - j[0]) ** 2
        y_distance = (i[1] - j[1]) ** 2
        distance = (x_distance + y_distance) ** (1/2) # 計算城鎮之間的距離
        distanceData.append(distance)
    
towns_distance = np.array(distanceData).reshape(towns,towns) # 重設陣列形狀以區隔城鎮
select = []
for i in range(totalSet): # 依照順序滿足需要設置的數量    
    townCover = []    
    for town in towns_distance:
        order = 0
        coverNum = 0
        for i in town:
            if i <= coverDistance: # 如果在覆蓋距離之內
                coverNum += population[order] # 將覆蓋的城鎮人口數加入此城鎮總覆蓋人口數
            order +=1
        townCover.append(coverNum) # 將設置在各城鎮可覆蓋的總人口數列入清單

    townNum = 0
    chooseValue = 0
    for i in townCover:
        if i > chooseValue: # 將最大值存到chooseValue，編號存到choose，且在最大值有兩個以上時，取編號小的
            chooseValue = i
            choose = townNum
        townNum += 1
    populationSum += chooseValue # 將最大值加入已覆蓋總人數
        
    covered = []
    for i in range(towns):
        if towns_distance[choose][i] <= coverDistance:
            covered.append(i) # 取得已覆蓋的城鎮
        
    for i in covered:
        population[i]=0 # 將已覆蓋城鎮可覆蓋的人口數設為0

    select.append(choose+1) # 編號由0~N改為1~N+1
    
for i in select:
    print(i,end=" ")
print(populationSum)