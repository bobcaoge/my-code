# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        ret = []
        products.sort()
        for i, c in enumerate(searchWord):
            buff = []
            for product in products:
                if len(product) > i and product[i] == c:
                    buff.append(product)
            products = buff
            ret.append(products[:3])
        return ret





def main():
    s = Solution()


if __name__ == "__main__":
    main()
