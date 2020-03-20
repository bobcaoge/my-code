# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import sys
from enum import Enum
from data_structure.stack import Stack


class Action(Enum):
        No = 0
        LToM = 1
        MToL = 2
        MToR = 3
        RToM = 4


def hanoi_problem(num, left, mid, right):
    """
    处理汉诺塔问题
    :param num: 汉诺塔最大层数
    :param left:
    :param mid:
    :param right:
    :return:
    """
    ls = Stack()
    ms = Stack()
    rs = Stack()
    ls.push(sys.maxsize)
    ms.push(sys.maxsize)
    rs.push(sys.maxsize)
    for i in reversed(range(1, num+1)):
        ls.push(i)

    record = [Action.No]
    step = 0
    while rs.size() != num+1:
        step += fStackTotStack(record, Action.MToL, Action.LToM, ls, ms, left, mid)
        step += fStackTotStack(record, Action.LToM, Action.MToL, ms, ls, mid, left)
        step += fStackTotStack(record, Action.RToM, Action.MToR, ms, rs, mid, right)
        step += fStackTotStack(record, Action.MToR, Action.RToM, rs, ms, right, mid)

    # print(ls)
    # print(ms)
    # print(rs)
    return step


def fStackTotStack(record, preNoAct, nowAct, fStack, tStack, from_which, to):
    """
    汉诺塔中的一步
    :param record: 对上一步行为的记录
    :param preNoAct:
    :param nowAct:
    :param fStack:
    :param tStack:
    :param from_which:
    :param to:
    :return:
    """

    if record[0] != preNoAct and fStack.peek() < tStack.peek():
        tStack.push(fStack.pop())
        print("Move {0} from {1} to {2}".format(tStack.peek(), from_which, to))
        record[0] = nowAct
        return 1
    return 0


def main():
    step = hanoi_problem(3, "left", "mid", "right")
    print(step)


if __name__ == '__main__':
    main()

