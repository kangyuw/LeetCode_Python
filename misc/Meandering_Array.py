# Meandering Array
# https://bit.ly/2HpDu3b

# O(N) space

def rearrange(arr, n):
    res = n * [None]
    head = 0
    tail = n - 1
    for i in range(n):
        # At even index put max element
        if i % 2 == 0:
            res[i] = arr[tail]
            tail -= 1
        else:
            res[i] = arr[head]
            head += 1
    return res

## testing code
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

n = len(arr)

print('Original Array:', arr)

rearrange(arr, n)

print('Modified Array:', arr)