# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Cashier(object):

    def __init__(self, n, discount, products, prices):
        """
        :type n: int
        :type discount: int
        :type products: List[int]
        :type prices: List[int]
        """
        self.num = 0
        self.n = n
        self.prices = {}
        self.discount = discount
        for i, id_of_product in enumerate(products):
            self.prices[id_of_product] = prices[i]

    def getBill(self, product, amount):
        """
        :type product: List[int]
        :type amount: List[int]
        :rtype: float
        """
        ret = 0
        self.num += 1
        for i, id_of_product in enumerate(product):
            ret += self.prices[id_of_product]*amount[i]
        if self.num == self.n:
            ret *= 1-self.discount/100.0
            self.num = 0
        return ret


def main():
    pass


if __name__ == "__main__":
    main()
