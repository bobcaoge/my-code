# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSubPath(self, head, root):
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """
        self.ret = False
        data = []
        while head:
            data.append(head.val)
            head = head.next
        def traverse(r, path):
            if path[-len(data):] == data:
                return True
            if not r:
                return False
            left = traverse(r.left, path+[r.val])
            right = traverse(r.right, path+[r.val])
            self.ret = left or right or self.ret
        traverse(root, [])
        return self.ret



def main():
    s = Solution()



if __name__ == "__main__":
    main()
