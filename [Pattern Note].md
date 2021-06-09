### QuickSort
```
def partition(self, nums, l, r) -> int:
    pi = random.randint(l, r)
    nums[l], nums[pi] = nums[pi], nums[l]
    p = nums[l]
    while l < r:
        while l < r and p <= nums[r]:
            r -= 1
        nums[l] = nums[r]
        while l < r and p >= nums[l]:
            l += 1
        nums[r] = nums[l]
    nums[l] = p
    return l

def quickSort(self, nums, l, r) -> int:
    N = len(nums)
    if l < r:
        pi = self.partition(nums, l, r)
        self.quickSort(nums, l, pi - 1)
        self.quickSort(nums, pi + 1, r)
    return nums
```

### Inorder Traversal
```
def inorderTraversal(self, root: TreeNode) -> List[int]:
    if root == None:
        return []
    st = []
    ans = []
    while len(st) > 0 or root != None:
        if root != None:
            st.append(root)
            root = root.left
        else:
            root = st[-1]
            st.pop()
            ans.append(root.val)
            root = root.right
    return ans
```

### Permutation
```
def permute(self, nums):
    res = []
    if not nums: return res
    
    def backtracking(res, item, nums):
        if len(item) == len(nums):  # Goal
            res.append(item)
            return
        for i in range(len(nums)):
            if nums[i] in item: continue  # Constrain
            item.append(nums[i])
            backtracking(res, item.copy(), nums)
            item.pop()

    backtracking(res, [], nums)
    return res
```

### Binary Search
```
def binarySearch(self, nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low+high) // 2
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            high = mid - 1
        elif target > nums[mid]:
            low = mid + 1
    return -1 # not found
```