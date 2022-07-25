import csv

class Time:
    def __init__(self, list): # 輸入為HH:MM:SS
        self.list = list
        timeList = self.list.split(":")
        self.hour = int(timeList[0]) # HH
        self.minute = int(timeList[1]) # MM
        self.second = int(timeList[2]) # SS
        self.secondPassed = self.hour*3600 + self.minute*60 +self.second # 拿來比較時間大小
    
periodGet = input()
period = periodGet.split()
begin = Time(period[0]) # 時間段開始
end = Time(period[1]) # 時間段結束

targetData = []
fileGet = "midterm.csv"
fileRead = open(fileGet, "r", encoding="utf-8")
read = csv.reader(fileRead)
for i in read:
    if i[6] != "SubmissionTime": # 不列入標題列
        data = Time(i[6])
        if end.secondPassed >= data.secondPassed >= begin.secondPassed: # 取得在時間段內的每筆資料中的所有資料
            targetData.append(i)
fileRead.close()

status = []
for j in range(1,5): # 題目1到4
    Acc, Com, Run, Tim, Wro = 0, 0, 0, 0, 0
    for i in targetData: # 為各種批改結果進行加總
        if int(i[2]) == j:
            if i[3] == "Accepted":
                Acc += 1
            elif i[3] == "Compile Error":
                Com += 1
            elif i[3] == "Runtime Error":
                Run += 1
            elif i[3] == "Time Limit Exceed":
                Tim += 1
            elif i[3] == "Wrong Answer":
                Wro +=1
    status.extend([Acc, Com, Run, Tim, Wro]) # 新增多種元素至清單中

for i in range(20): # 4個題目 * 5種結果
    if (i+1)%5 == 0: # 5種批改結果為一組
        print(status[i], end=";")
    else:
        print(status[i], end=" ")