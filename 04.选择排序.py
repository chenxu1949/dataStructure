l = [23,11,4,56,43,32,67,45]

def choose_sort(list_l):
    n = len(list_l)
    for i in range(n-1):           # 外层循环选择一个数作比较，对第i个元素进行选择
        min_index = i              # 假设第i个元素为最小的数
        for k in range(i+1,n):
            if list_l[min_index] > list_l[k]:   # 内层循环用前面的min_num和k比较
                min_index = k      # 需要重新将第k个数假设为最小数
        if min_index != i:
            list_l[min_index],list_l[i] = list_l[i],list_l[min_index]

choose_sort(l)
print(l)

