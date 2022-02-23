class Solution:
    def singleNumber(self, nums):
        count = {}
        for s in nums:
            if s in count:
                count[s] += 1
            else:
                count[s] = 1
        return list(count.keys())[list(count.values()).index(1)]
#But really, the point of this is to learn the xor operator
class Solution:
    def singleNumber(self, nums):
        pass
#Test Cases
sol = Solution()
print(sol.singleNumber([2,2,1]))
print(sol.singleNumber([4,1,2,1,2]))
