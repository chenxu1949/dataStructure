l = [23,11,4,56,43,32,67,45]
def insert_sort(list_l):
    n = len(list_l)
    for i in range(1,n):         # 抽牌的下标取值范围
        for k in range(i,0,-1):  # 抽到的牌和左边的牌比较，左边牌下标的范围
            if list_l[k] < list_l[k-1]:
                list_l[k],list_l[k-1] = list_l[k-1],list_l[k]
            else:
                break
insert_sort(l)
print(l)

from gensim import corpora,models
a = models.tfidfmodel





