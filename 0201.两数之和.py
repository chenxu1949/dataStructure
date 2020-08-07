# 暴力法
# class Solution(object):
#     def twoSum(self, nums, target):
#         for k in range(len(nums)):
#             for i in range(len(nums) - 1, -1, -1):
#                 if nums[k] + nums[i] == target and k!=i:
#                     a = [k, i]
#                     return a


# 哈希表法
class Solution(object):
    def twoSum(self, nums, target):
        dic = {}
        for i, num in enumerate(nums):
            if num in dic:
                return [dic[num], i]
            else:
                dic[target - num] = i

# li = [1,3,5,7]
# a = 8
# dic = {}
# def func(l,a):
#     for i,k in enumerate(l):
#         if k in dic:
#             print([dic[k],i])
#         else:
#             dic[a - k] = i
# func(li,a)


# 切片法
# class Solution:
#     def twoSum(self, nums, target):
#         for i in range(len(nums)):
#             if target-nums[i] in nums[i+1:]:
#                 return [i,nums.index(target-nums[i],i+1)]
