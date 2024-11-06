# nums = [1,2,3,4,5,6], k = 4
class Solution:
    def findMaxAverage(self, nums, k):
        cur_sum = sum(nums[:k])
        max_sum = cur_sum
        for i in range(k,len(nums)):
            cur_sum += nums[i]
            cur_sum -= nums[i-k]
            max_sum = max(cur_sum,max_sum)
        return max_sum / k
obj = Solution()
print(obj.findMaxAverage([1,2,3,4,5,6],4))
            
        