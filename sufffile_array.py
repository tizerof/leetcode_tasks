class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        
    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        from random import shuffle
        a = list.copy(self.nums)
        shuffle(a)
        return a


# Your Solution object will be instantiated and called as such:
nums = [1,2,3]
obj = Solution(nums)
param_1 = obj.shuffle()
param_2 = obj.reset()
param_3 = obj.shuffle()
print(param_1, param_2, param_3)