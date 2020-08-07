l = [23,11,4,56,43,32,67,45]

def pop_sort(list_l):

    n = len(list_l)
    for i in range(n-1):        # 冒泡次数
        num = 0                 # 标志位，如果num没变，则说明前面的已经排好序了，后边的冒泡就不用再去比较
        for k in range(n-1-i):  # 前置比较对象的取值范围
            if list_l[k] > list_l[k+1]:
                list_l[k],list_l[k+1] = list_l[k+1],list_l[k]
            num += 1
        if num == 0:
            break

pop_sort(l)
print(l)





# l = [(3,1),(2,1),(5,6),(1,4),(3,7)]
# print(sorted(l,key=lambda x:x[0]))
