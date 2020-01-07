class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        duplicate = -1
        dismatch = -1
        for i in range(n):
            if nums[abs(nums[i]) - 1] < 0:
                duplicate = abs(nums[i]) 
            else:
                nums[abs(nums[i]) - 1] *= -1
        for i in range(n):
            if nums[i] > 0:
                dismatch = i + 1
        return [duplicate, dismatch]
