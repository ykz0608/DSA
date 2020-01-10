class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one = 0; two = 0; three = 0
        for i in range(len(nums)):
            # print one, two, three
            two |= nums[i] & one  # two爲1時，不管A[i]爲什麽，two都爲1
            # print two
            one = nums[i] ^ one  # 異或操作，都是1就進位
            # print one
            three = ~(one & two) # 以下三步的意思是：如果one和two都爲1時，就清0，反之則保持原來狀態。
            one &= three
            two &= three
            # print one, two, three
            # print '----'
        return one
