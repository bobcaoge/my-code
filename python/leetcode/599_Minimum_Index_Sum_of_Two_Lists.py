# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        m1 = {}
        for index, value in enumerate(list1):
            m1[value] = index
        min_index = -1
        ret = []
        for value, key in enumerate(list2):
            if m1.get(key, -1) != -1:
                sum_of_index = value + m1[key]
                if min_index == -1:
                    min_index = sum_of_index
                    ret = [key]
                else:
                    if min_index == sum_of_index:
                        ret.append(key)
                    elif min_index > sum_of_index:
                        ret = [key]
        return ret

    def findRestaurant3(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        m1 = {}
        m2 = {}
        for index, value in enumerate(list1):
            m1[value] = index
        for index, value in enumerate(list2):
            m2[value] = index
        min_index = -1
        ret = []
        for key, value in m1.items():
            if m2.get(key, -1) != -1:
                sum_of_index = value + m2[key]
                if min_index == -1:
                    min_index = sum_of_index
                    ret = [key]
                else:
                    if min_index == sum_of_index:
                        ret.append(key)
                    elif min_index > sum_of_index:
                        ret = [key]
        return ret



    def findRestaurant2(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        common = list(set(list1) & set(list2))
        if len(common) == 1:
            return common
        m = {}
        min_key = -1
        for c in common:
            key = list1.index(c)+list2.index(c)
            if m.get(key, 0) == 0:
                m[key] = [c]
            else:
                m[key].append(c)
            if min_key == -1:
                min_key = key
            else:
                min_key = key if min_key > key else min_key
        return m[min_key]

    def findRestaurant1(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        common = list(set(list1) & set(list2))
        if len(common) == 1:
            return common
        commons = [[list1.index(c)+list2.index(c), c] for c in common]
        commons.sort()
        ret = [commons[0][1]]
        for c in commons[1:]:
            if c[0] == commons[0][0]:
                ret.append(c[1])
            else:
                break
        return ret

def main():
    s = Solution()
    print(s.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["KFC","Burger King","Tapioca Express","Shogun"]))
    print(s.findRestaurant(["dixyp","uq","q","KFC"], ["yl","fjugc","rlni","dixyp","uq","q","KFC"]))

if __name__ == "__main__":
    main()
