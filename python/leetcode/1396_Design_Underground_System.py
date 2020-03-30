# #usr#bin#python3.6
# -*- coding:utf-8 -*-


class UndergroundSystem(object):

    def __init__(self):
        self.time_of_stations = {} # (时间，次数)
        self.person = {}  # {id: (station checked in, t)}


    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.person[id] = (stationName, t)


    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        station_in, time_in = self.person[id]
        if not self.time_of_stations.get((station_in, stationName)):
            self.time_of_stations[(station_in, stationName)] = (t - time_in, 1)
        else:
            total_time, times = self.time_of_stations[(station_in, stationName)]
            self.time_of_stations[(station_in, stationName)] = (t - time_in+total_time, times+1)

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        total_time, times = self.time_of_stations[(startStation, endStation)]
        return total_time*1.0/times




def main():
    undergroundSystem = UndergroundSystem()
    undergroundSystem.checkIn(45, "Leyton", 3)
    undergroundSystem.checkIn(32, "Paradise", 8)
    undergroundSystem.checkIn(27, "Leyton", 10)
    undergroundSystem.checkOut(45, "Waterloo", 15)
    undergroundSystem.checkOut(27, "Waterloo", 20)
    undergroundSystem.checkOut(32, "Cambridge", 22)
    print(undergroundSystem.getAverageTime("Paradise", "Cambridge"))       ## return 14.0. There was only one travel from "Paradise" (at time 8) to "Cambridge" (at time 22)
    print(undergroundSystem.getAverageTime("Leyton", "Waterloo") )         ## return 11.0. There were two travels from "Leyton" to "Waterloo", a customer with id=45 from time=3 to time=15 and a customer with id=27 from time=10 to time=20. So the average time is ( (15-3) + (20-10) ) # 2 = 11.0
    undergroundSystem.checkIn(10, "Leyton", 24)
    print(undergroundSystem.getAverageTime("Leyton", "Waterloo")  )        ## return 11.0
    undergroundSystem.checkOut(10, "Waterloo", 38)
    print(undergroundSystem.getAverageTime("Leyton", "Waterloo"))


if __name__ == "__main__":
    main()
