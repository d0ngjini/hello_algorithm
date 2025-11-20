def solution(info, n, m):
    answer = 0
    dp = {}
    dp[(0,0,0)] = 0
    
    for i in range(len(info)):
        a_trace, b_trace = info[i]
        new_dp = {}
        
        for (idx, a, b), result in dp.items():
            if idx != i:
                continue
                
            if a + a_trace < n:
                key = (i + 1, a + a_trace, b)
                val = a + a_trace
                new_dp[key] = min(new_dp.get(key, float('inf')), val)
                
            if b + b_trace < m:
                key = (i + 1, a, b + b_trace)
                val = a
                new_dp[key] = min(new_dp.get(key, float('inf')), val)
                
                
        dp.update(new_dp)
    
    answer = min((v for (idx, a, b), v in dp.items() if idx == len(info)), default=float('inf'))
    return answer if answer != float('inf') else -1