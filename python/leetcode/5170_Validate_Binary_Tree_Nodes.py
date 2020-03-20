# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        """
        :type n: int
        :type leftChild: List[int]
        :type rightChild: List[int]
        :rtype: bool
        """
        parents = {}
        unconnected = [True]*n
        for i in range(n):
            left = leftChild[i]
            if left != -1:
                if parents.get(i, -1) == left or parents.get(left, -1) != -1:
                    return False
                parents[left] = i
                unconnected[left] = False
            right = rightChild[i]
            if right != -1:
                if parents.get(i, -1) == right or parents.get(right, -1) != -1:
                    return False
                parents[right] = i
                unconnected[right] = False

        return sum(unconnected) == 1




def main():
    s = Solution()
    print(s.validateBinaryTreeNodes( n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]))
    print(s.validateBinaryTreeNodes(n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]))
    print(s.validateBinaryTreeNodes(n = 2, leftChild = [1,0], rightChild = [-1,-1]))
    print(s.validateBinaryTreeNodes(n = 6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1]))


if __name__ == "__main__":
    main()
