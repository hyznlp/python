def find(alist, item):
    find = False
    first = 0
    last = len(alist) - 1
    while last > first:
        middle_index = (first + last) // 2
        if alist[middle_index] < item:
            first = middle_index + 1
        elif alist[middle_index] > item:
            last = middle_index -1
        else:
            find = True
            break
    return find
alist = [1, 2,3,4,5,6,7,8,9]
print(find(alist, 3))