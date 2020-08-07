# l = [1,1,2]
# def func(list_l):
#     set_l = list(set(list_l))
#     print(set_l)
#     print(len(set_l))
# func(l)

# l = [1,1,2]
# def removeDuplicates(nums):
#     k = 0
#     for i, num in enumerate(nums):
#         if k < 1 or num != nums[k - 1]:
#             if i != k:
#                 nums[k] = num
#             k += 1
#     print(k)
#
# removeDuplicates(l)


def removeDuplicates(nums):
    i = 0
    for num in nums:
        if nums[i] != num:
            i += 1
            nums[i] = num
    print(len(nums))
    return len(nums) and i+1

removeDuplicates([1,1,2])
