# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def sampleStats(self, count):
        """
        :type count: List[int]
        :rtype: List[float]
        """
        ret = [1000, -1, 0, 0, 0]
        number = sum(count)
        sum_of_samples = 0.0
        mod = 0
        for i, num in enumerate(count):
            ret[0] = min(i if num > 0 else 1000, ret[0])
            ret[1] = max(i if num > 0 else -1, ret[1])
            sum_of_samples += i*num
            if num > count[mod]:
                mod = i
        ret[2] = sum_of_samples/number
        ret[-1] = mod
        middles = [number/2+1]
        if number % 2 == 0:
            middles.append(number/2)
        sum_of_middles = 0.0
        for mid in middles:
            cur_nums = 0
            for i, num in enumerate(count):
                cur_nums += num
                if cur_nums >= mid:
                    sum_of_middles += i
                    break
        ret[3] = sum_of_middles / len(middles)
        return ret











def main():
    s = Solution()


if __name__ == "__main__":
    main()
