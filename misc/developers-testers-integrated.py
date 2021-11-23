def integrate(d, t, n):
    # 2 2-d dp tables
    # dpT[n+1][t]: how many combination with t Ts in the end of a length n list

    dpT = [[0 for _ in range(t)] for _ in range(n+1)]
    dpD = [[0 for _ in range(d)] for _ in range(n+1)]

    # base case: n = 0: 0 possible combination
    
    # transition

    for i in range(1,n+1):
        for jt in range(t):
            # transition across groups
            dpD[i][1] += dpT[i-1][jt]
            if jt == i:
                dpT[i][jt] = 1
            else:
                # transition within same group
                dpT[i][jt] = dpT[i-1][jt-1]
        for jd in range(d):
            dpT[i][1] += dpD[i-1][jd]
            if jd == i:
                dpD[i][jd] = 1
            else:
                dpD[i][jd] = dpD[i-1][jd-1]    

    result = 0
    for i in range(t):
        result += dpT[n][i]
    for i in range(d):
        result += dpD[n][i]
    print(dpT)
    print(dpD)
    return result


d = 3
t = 2
n = 4

res = integrate(d,t,n)
print(res)