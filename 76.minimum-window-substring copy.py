
import collections
import sys


def minWindow(s, t):

    # 初始化字母表
    table = collections.Counter(t)

    # 初始化 Sliding Window
    begin = 0
    end = 0
    counter = len(t)
    cur_len = sys.maxsize

    # Start Sliding Window
    while end < len(s):
        endchar = s[end]

        # 在字母表中找到對應的字母
        if endchar in table:
            table[endchar] -= 1
            if table[endchar] == 0:
                counter -= 1
        end += 1

        # 如果新 Window 比之前都要小
        while counter == 0:
            if end - begin < cur_len:
                cur_len = end - begin

            # 如果 s 開頭的字元 不在字母表中: 去掉它
            startchar = s[begin]

            if startchar in table:
                table[startchar] += 1
                if table[startchar] > 0:
                    counter += 1

            begin += 1
        print(begin, end, table)

    return s[begin:end]


S = "aa"
T = "aa"
table = collections.Counter(T)
print(len(table))