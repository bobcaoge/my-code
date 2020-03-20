# /usr/bin/python3.6
# -*- coding:utf-8 -*-
class Node(object):
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent

    def __str__(self):
        return "{}, {}".format(self.value, self.parent)

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        m = {}
        for i, equation in enumerate(equations):
            parent, child = equation
            parent_node = m.get(parent, None)
            child_node = m.get(child, None)
            if parent_node:
                if not child_node:
                    m[child] = Node(values[i], parent)
                else:
                    child_node.parent = parent
                    child_node.value = values[i]
            else:
                if not child_node:
                    m[parent] = Node(1.0, "-1")
                    m[child] = Node(values[i], parent)
                else:
                    m[parent] = Node(1.0/values[i], child)
        # print(m.keys())
        # for key, value in m.items():
        #     print(key, value)

        ret = []

        for query in queries:
            a, b = query
            # if a == b:
            #     ret.append(1)
            #     continue
            parent_node_of_a = m.get(a, None)
            parent_node_of_b = m.get(b, None)
            if not parent_node_of_a or not parent_node_of_b:
                ret.append(-1.0)
                continue
            num1 = 1.0
            while parent_node_of_a.parent != "-1":
                num1 *= parent_node_of_a.value
                parent_node_of_a = m.get(parent_node_of_a.parent)

            num2 = 1.0
            while parent_node_of_b.parent != "-1":
                num2 *= parent_node_of_b.value
                parent_node_of_b = m.get(parent_node_of_b.parent)
            if parent_node_of_a == parent_node_of_b:
                ret.append(num2/num1)
            else:
                ret.append(-1)
        return ret



def main():
    s = Solution()
    print(s.calcEquation(equations = [ ["a", "b"], ["b", "c"] ],
                         values = [2.0, 3.0],
                         queries =  [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]))
    print(s.calcEquation([["a","e"],["b","e"]],
                         [4.0,3.0],
                         [["a","b"],["e","e"],["x","x"]]))

    print(s.calcEquation([["a","b"],["e","f"],["b","e"]],
                         [3.4,1.4,2.3],
                         [["b","a"],["a","f"],["f","f"],["e","e"],["c","c"],["a","c"],["f","e"]]))


if __name__ == "__main__":
    main()
