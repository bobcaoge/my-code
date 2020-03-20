# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        s = [gas[i]-cost[i] for i in range(len(gas))]
        if sum(s) < 0:
            return -1

        ret = -1
        sum_ = 0
        # print(s)
        for i, num in enumerate(s):
            sum_ += num
            if num >= 0:
                if ret == -1:
                    ret = i
            else:
                if sum_ < 0:
                    sum_ = 0
                    ret = -1
        return ret

    def canCompleteCircuit1(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        length_of_gas_station = len(gas)
        for i in range(len(gas)):
            if gas[i] >= cost[i]:
                cur_gas_station = i
                sum_of_gas_in_car = gas[cur_gas_station]
                cur_gas_station = (cur_gas_station+1) % length_of_gas_station

                for j in range(len(cost)-1):
                    last_gas_station = (cur_gas_station - 1 + length_of_gas_station) % length_of_gas_station
                    sum_of_gas_in_car -= cost[last_gas_station]
                    if sum_of_gas_in_car < 0:
                        break
                    sum_of_gas_in_car += gas[cur_gas_station]
                    cur_gas_station = (cur_gas_station+1) % length_of_gas_station
                last_gas_station = (cur_gas_station - 1 + length_of_gas_station) % length_of_gas_station
                if sum_of_gas_in_car >= cost[last_gas_station]:
                    return cur_gas_station
        return -1


def main():
    s = Solution()
    print(s.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))
    print(s.canCompleteCircuit([3,3,4], [3,4,4]))
    print(s.canCompleteCircuit([5,1,2,3,4], [4,4,1,5,1]))
    print(s.canCompleteCircuit([5,5,1,3,4], [8,1,7,1,1]))


if __name__ == "__main__":
    main()
