# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        def construct(pre_start, pre_end, post_start, post_end):
            if pre_start> pre_end:
                return None
            if pre_start == pre_end:
                return TreeNode(pre[pre_start])
            s1 = set()
            s2 = set()
            offset = 0
            for i in range(1, pre_end-pre_start+1):
                s1.add(pre[pre_start+i])
                s2.add(post[post_start+i-1])
                if s1 == s2:
                    offset = i
                    break
            cur = TreeNode(pre[pre_start])
            cur.left = construct(pre_start+1, pre_start+offset, post_start, post_start+offset-1)
            cur.right = construct(pre_start+offset+1, pre_end, post_start+offset, post_end-1)
            return cur
        return construct(0, len(pre)-1, 0, len(post)-1)



def main():
    s = Solution()
    print(s.constructFromPrePost( pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]))


if __name__ == "__main__":
    main()
