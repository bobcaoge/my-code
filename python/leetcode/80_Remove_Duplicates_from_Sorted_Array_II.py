# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        front = length
        for i in range(1, length-1):
            if nums[i-1] == nums[i] == nums[i+1]:
                front = i+1
                break
        if front == length:
            return length
        ret = front
        time = 2
        last = nums[front]
        back = front
        while back < length:
            if last != nums[back] or last == nums[back] and time < 2:
                nums[front] = nums[back]
                time = 1 if last != nums[back] else time+1
                last = nums[front]
                front += 1
                ret += 1
            back += 1
        # print(nums)
        return ret

    def removeDuplicates1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if not nums:
        #     return 0
        length = len(nums)
        front = length
        for i in range(1, length-1):
            if nums[i-1] == nums[i] == nums[i+1]:
                front = i+1
                break
        if front == length:
            return length
        ret = front
        time = 2
        last = nums[front]
        back = front
        while back < length:
            if last != nums[back]:
                nums[front] = nums[back]
                time = 1
                last = nums[front]
                front += 1
                ret += 1
            else:
                if time < 2:
                    nums[front] = nums[back]
                    time += 1
                    front += 1
                    ret += 1
            back += 1
        print(nums)
        return ret




def main():
    s = Solution()
    # print(s.removeDuplicates([0,0,1,1,1,1,2,3,3]))
    # print(s.removeDuplicates([1,1,1,2,2,3]))
    print(s.removeDuplicates([1]))
    print(s.removeDuplicates([1,1,1,2,2,2,3,3,3,4,4,4]))
    print(s.removeDuplicates([]))



if __name__ == "__main__":
    main()
