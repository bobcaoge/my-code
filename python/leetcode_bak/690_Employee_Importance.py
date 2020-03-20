# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates


class Solution(object):

    def getImportance(self, employees, id):
        """
        :type id: int
        :rtype: int
        """
        ret = 0
        m = {}
        for employee in employees:
            m[employee.id] = [employee.importance, employee.subordinates]
        if m.get(id, None):
            buffer = m[id][1]
            ret += m[id][0]
        else:
            return 0
        while buffer:
            cur = buffer.pop()
            ret += m[cur][0]
            buffer += m[cur][1]

        return ret



def main():
    s = Solution()


if __name__ == "__main__":
    main()
