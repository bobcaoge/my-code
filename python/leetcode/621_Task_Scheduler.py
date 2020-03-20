# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        record = [0]*26
        for task in tasks:
            record[ord(task)-65]+=1

        # 获得同种任务最多的个数及其索引
        max_num = max(record)
        index = -1
        for i in range(26):
            if record[i] == max_num:
                index = i
                break

        num = 0
        for i in record:
            if i == max_num:
                num += 1
        ret = (n+1)*(record[index]-1)+num

        return max(ret, len(tasks))


def main():
    s = Solution()
    print(s.leastInterval(['A', 'A','A','B','B','B','C','C','C'], 1))



if __name__ == "__main__":
    main()
