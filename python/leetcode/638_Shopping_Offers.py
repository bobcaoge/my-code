# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    min_cost = 2**31-1

    def find_one(self, price, special, needs, costs):
        offer_can_be_used = False
        for i in range(len(special)):
            cur_need = [x for x in needs]
            flag = True
            cur_special = special[i]
            for index, need in enumerate(needs):
                if need < cur_special[index]:
                    flag = False
                    break
                cur_need[index] -= cur_special[index]
            if flag:
                offer_can_be_used = True
                self.find_one(price, special, cur_need, costs+cur_special[-1])
        if not offer_can_be_used:
            for index, need in enumerate(needs):
                costs += need*(price[index])
            self.min_cost = min(self.min_cost, costs)

    def filter_of_specials(self, specials, prices):
        filted_specials = []
        for special in specials:
            cost = 0
            for index, price in enumerate(prices):
                cost += special[index]*price
            if cost > special[-1]:
                filted_specials.append(special)
        return filted_specials

    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        self.min_cost = 2**31-1
        self.memo = set()
        self.find_one(price, self.filter_of_specials(special, price), needs, 0)
        return self.min_cost


def main():
    s = Solution()
    print(s.shoppingOffers([2,5], [[3,0,5],[1,2,10]], [3,2]))
    print(s.shoppingOffers([2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1]))
    print(s.shoppingOffers([0,0,0],[[1,1,0,4],[2,2,1,9]],[1,1,1]))
    print(s.shoppingOffers([1,1,1],[[1,1,0,0],[2,2,1,9]], [1,1,0]))
if __name__ == "__main__":
    main()
