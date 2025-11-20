def solution(info, n, m):
    # 보자마자 무슨 의도의 문제인지 알아야 함
    
    # 모든 경우의 수 체크?
    # 이중 포인터 같긴한데
    # 항상 b를 먼저 진행시키고 a를 체크 -> 그리디 접근법 실패
    
    # dp
    dp = {}
    dp[(0, 0, 0)] = 0
    
    for i in range(len(info)):
        a_trace, b_trace = info[i]
        new_dp = {}
        
        for (idx, a, b), a_total in dp.items():
            if idx != i:
                continue
            
            if a + a_trace < n:
                new_key = (i + 1, a + a_trace, b)
                new_total = a + a_trace
                new_dp[new_key] = min(new_dp.get(new_key, float('inf')), new_total)
                
            if b + b_trace < m:
                new_key = (i + 1, a, b + b_trace)
                new_total = a
                new_dp[new_key] = min(new_dp.get(new_key, float('inf')), new_total)
        
        dp.update(new_dp)
        
        
    answer = min((v for (i, a, b), v in dp.items() if i == len(info)), default=float('inf'))
    return answer if answer != float('inf') else -1