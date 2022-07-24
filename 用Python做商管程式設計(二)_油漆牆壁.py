missionGet = input() # 取得牆壁n面、m次油漆
mission = missionGet.split() 
wallNum = int(mission[0])
paintNum = int(mission[1])

status = {}
for i in range(wallNum): # 將所有牆面設為顏色1的狀態
    status.update({i+1:1})

action = []
order = []
for i in range(paintNum): # 取得油漆的方式
    actionGet = input()
    actionSplit = actionGet.split()
    action.append(actionSplit)
    paintRange = int(action[i][1]) - int(action[i][0]) + 1 # 計算油漆了幾面牆
    for j in range(paintRange):
        wall = int(action[i][0]) + j
        color = int(action[i][2])
        status.update({wall:color}) # 將牆面的狀態紀錄於status
    order.append(color) # 取得油漆顏色的順序

colorList = {}
for i, j in status.items(): # 計算各顏色牆壁出現的數量
    if j not in colorList:
        colorList[j] = 1
    else:
        colorList[j] += 1

for i in order: # 按照油漆顏色的順序打印出各顏色牆壁出現的數量
    if i != paintNum:
        print(colorList[i], i, end=";")
    else:
        print(colorList[i], i)