# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import collections


class Solution(object):
    def deleteTreeNodes(self, nodes, parent, value):
        """
        :type nodes: int
        :type parent: List[int]
        :type value: List[int]
        :rtype: int
        """
        self.children = collections.defaultdict(list)
        for i, num in enumerate(parent):
            self.children[num].append(i)

        def dfs(i):
            sum_of_cur_tree = value[i]
            to_remove = []
            for child in self.children[i]:
                sum_of_sub_tree = dfs(child)
                if sum_of_sub_tree == 0:
                    to_remove.append(child)
                sum_of_cur_tree += sum_of_sub_tree
            for r in to_remove:
                self.children[i].remove(r)
            return sum_of_cur_tree
        if dfs(0) == 0:
            return 0

        def get_num(i):
            ret = 1
            for child in self.children[i]:
                ret += get_num(child)
            return ret
        return get_num(0)


def main():
    s = Solution()
    print(s.deleteTreeNodes(nodes = 7, parent = [-1,0,0,1,2,2,2], value = [1,-2,4,0,-2,-1,-1]))


if __name__ == "__main__":
    main()
