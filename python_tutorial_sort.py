#冒泡排序
def sort1(alist):
    for j in range(len(alist)-1):
        for i in range(len(alist)-1-j):#两两比较次数
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
    return alist


#选择排序
def sort2(alist):
    for j in range(len(alist)-1):
        max_index = 0
        for i in range(1, len(alist)-j):
            if alist[max_index] < alist[i]:
                max_index = i
        alist[len(alist)-1-j], alist[max_index] = alist[max_index], alist[len(alist)-1-j]

    return alist


#插入排序
def sort3(alist):
    # i = 1
    # if alist[i-1] > alist[i]:
    #     alist[i-1], alist[i] = alist[i], alist[i-1]
    # else:
    #     i += 1
    #
    # i = 2
    # if alist[i-1] > alist[i]:
    #     alist[i-1], alist[i] = alist[i], alist[i-1]
    #     i -= 1
    # else:
    #     break
    for i in range(1, len(alist)):
        while i > 0:
            if alist[i - 1] > alist[i]:
                alist[i - 1], alist[i] = alist[i], alist[i - 1]
                i -= 1
            else:
                break
    return alist


#希尔排序
def sort4(alist):
    gap = len(alist) // 2
    while gap >= 1:
        for i in range(gap, len(alist)):
            while i > 0:
                if alist[i - gap] > alist[i]:
                    alist[i - gap], alist[i] = alist[i], alist[i - gap]
                    i -= gap
                else:
                    break
        gap //= 2
    return alist


#快速排序
def sort5(alist, start, end):
    low = start
    high = end
    # mid = alist[start]

    if low > high:
        return

    mid = alist[start]
    while low < high:
        while low < high:
            if alist[high] > mid:
                high -= 1
            else:
                alist[low] = alist[high]
                break
        while low < high:
            if alist[low] < mid:
                low += 1
            else:
                alist[high] = alist[low]
                break
        if low == high:
            alist[low] = mid
            break

    sort5(alist, start, high-1)
    sort5(alist, low+1, end)
    return alist

alist = [6,1,2,7,9,3,4,5,10,8]
print(sort5(alist, 0, len(alist)-1))
