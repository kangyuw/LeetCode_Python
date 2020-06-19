
def mincostTickets(days, costs):
    dp = [0] * (days[-1] + 1)
    j = 0
    for i in range(1, days[-1] + 1):
        if i != days[j]:
            dp[i] = dp[i-1]
        else:
            dp[i] = min(dp[i-1] + costs[0],
                        dp[max(i-7, 0)] + costs[1],
                        dp[max(i-30, 0)] + costs[2])
            j += 1
        print(dp)
    return dp[-1]


days = [1, 4, 6, 7, 8, 20]
costs = [2, 7, 15]

mincostTickets(days, costs)
