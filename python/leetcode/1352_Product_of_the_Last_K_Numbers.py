# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class ProductOfNumbers(object):

    def __init__(self):
        self.nums = [1]
        self.products = [1]
        self.nums_of_positive_from_tail = 1

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.nums.append(num)
        self.products.append(num*self.products[-1])
        if self.products[-1] == 0:
            self.products[-1] = num
        if self.products[-1] == 0:
            self.nums_of_positive_from_tail = 0
        else:
            self.nums_of_positive_from_tail += 1

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        if self.nums_of_positive_from_tail < k:
            return 0
        if self.products[-k-1] == 0:
            return self.products[-1]
        else:
            return self.products[-1]/self.products[-k-1]



def main():
    s = ProductOfNumbers()
    for num in [3, 0, 2, 5,4]:
        s.add(num)
    print(s.products)


if __name__ == "__main__":
    main()
