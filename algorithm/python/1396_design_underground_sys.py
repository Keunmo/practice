# https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:

    def __init__(self):
        self.data = {}      # { id1:[[in_sta,t,out_sta],[in_sta,t,out_sta], ... ], id2 = [[in,t,out], [], []], ... }

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id in self.data:
            self.data[id].append([stationName, t, 0])
        else:
            self.data[id]=[[stationName, t, 0]]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        for i in self.data[id]:
            if i[2] == 0:
                i[2] = stationName
                i[1] = t - i[1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time = 0
        count = 0
        for i in list(self.data.values()):
            for j in [x for x in i]:
                if j[0] == startStation and j[2] == endStation:
                    count += 1
                    time += j[1]
        return time / count



# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)