"""
bubble sort
Average:  O(N^2)
Best:     O(N)
Worst:    O(N^2)
Space:    O(1)
Method:   In-place
Stable:   Stable
"""
def bubble_sort(items, comp=lambda x,y: x<y):
    items = items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
            if not swapped:
                break
    return items

"""
select sort
Average:  O(N^2)
Best:     O(N^2)
Worst:    O(N^2)
Space:    O(1)
Method:   In-place
Stable:   Unstable
"""
def select_sort(items, comp=lambda x,y: x<y):
    items = items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items

"""
insertion sort
Average:  O(N^2)
Best:     O(N)
Worst:    O(N^2)
Space:    O(1)
Method:   In-place
Stable:   Stable
"""
def insertion_sort(items, comp=lambda x,y: x<y):
    items = items[:]
    for i in range(len(items) - 1):
        tmp = items[i] # the number to insert
        j = i
        # start from the right, find smaller number
        while ( j > 0 and tmp < items[j - i]):
            items[j] = items[j-1]
            j -= 1
        
        if (j != i):
            items[j] = tmp
    return items

"""
merge sort
Average:  O(N logN)
Best:     O(N logN)
Worst:    O(N logN)
Space:    O(N)
Method:   Out-Place
Stable:   Unstable

pusedo code:
sort(nums, lo, hi):
    mid = lo + (hi - lo) // 2
    sort(nums, lo, mid)
    sort(nums, mid + 1, hi)
    merge(nums, lo, mid, hi)
"""
def merge(items1, items2, comp=lambda x,y: x<y):
    items = []
    index1, index2 = 0, 0
    while index1 < len(items1) and index2 < len(items2):
        if comp(items1[index1], items[index2]):
            items.append(items1[index1])
            index1 += 1
        else:
            items.append(items2[index2])
            index2 += 1
    items += items1[index1:]
    items += items2[index2:]
    return items

def _merge_sort(items, comp):
    if len(items) < 2:
        return items
    mid = len(items) // 2
    left = _merge_sort(items[:mid], comp)
    right = _merge_sort(items[mid:], comp)
    return merge(left, right, comp)

def merge_sort(items, comp):
    return _merge_sort(list(items), comp)

"""
quick sort
Average:  O(N logN)
Best:     O(N logN)
Worst:    O(N^2)
Space:    O(logN)
Method:   In-Place
Stable:   Unstable

pusedo code:
sort(nums, lo, hi):
    p = partition(nums, lo, hi)
    sort(nums, lo, p - 1)
    sort(nums, p + 1, hi)
"""
def partition(items, left, right):
    pivot = left
    index = pivot + 1
    for i in range(right+1):
        if (items[i] < items[pivot]):
            items[i], items[index] = items[index], items[i]
            index += 1
    items[pivot], items[index-1] = items[index-1], items[pivot]
    return index - 1

def _quick_sort(items, left, right):
    if left < right:
        partitionIndex = partition(items, left, right)
        _quick_sort(items, left, partitionIndex - 1)
        _quick_sort(items, partitionIndex + 1, right)
    return items

def quick_sort(items):
    items = items[:]
    return _quick_sort(list(items), 0, len(items) -1)