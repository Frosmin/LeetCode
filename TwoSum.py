
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range (len(nums)):
                if target == nums[i] + nums[j] and i != j:
                    return [i, j]
           
           
           
solucion = Solution()   
    
print(solucion.twoSum([3,2,3], 6)) 