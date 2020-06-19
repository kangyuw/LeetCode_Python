from collections import defaultdict
from bisect import bisect_left


def longestCommonSubsequence(text1: str, text2: str) -> int:
    if text1 == text2:  # 完全一樣
        return len(text1)
    if not set(text1).intersection(text2):  # 完全沒有交集
        return 0

    d = defaultdict(list)  # 遇到不存在的 key 會回傳 default
    m, n = len(text1), len(text2)
    for i in range(n-1, -1, -1):  # 從 n-1 到 0
        d[text2[i]].append(i)  # 倒著建立每個字的座標

    nums = []
    for c in text1:
        if c in d:
            nums.extend(d[c])  # extend: 將內容直接放進原 list 中, 而非只是接在後面

    ans = []
    for num in nums:
        idx = bisect_left(ans, num)
        if idx == len(ans):
            ans.append(num)
        else:
            ans[idx] = num
    return len(ans)

res = longestCommonSubsequence("serdxtvguirdvgbnjmk", "rdtfyghijokxrdcfvgbh")
print(res)
