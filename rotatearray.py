class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        for s in range(k):
            nums.pop()
            nums.insert(0, nums[-1])