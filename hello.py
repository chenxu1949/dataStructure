book_id1 = [[10,1],[11,1]]
book_id2 = [[5,2],[8,2]]
book_id3 = [[20,3],[8,3]]
book_list = []
line = max(len(book_id1),len(book_id2),len(book_id3))
for i in range(line):
    a = book_id1.pop(i)
    b = book_id2.pop(i)
    c = book_id3.pop(i)
    book_list.append(a)
    book_list.append(b)
    book_list.append(c)
print(book_list)


# ,[12,1],[13,1]
# ,[30,3]