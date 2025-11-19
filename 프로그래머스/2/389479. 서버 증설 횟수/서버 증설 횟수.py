def solution(players, m, k):
    # 증설된 서버가 사라지는 시간을 체크해야한다.. -> 미리 배열로 서버 개수를 기록한다면?
    server_count_list = [0] * 24
    expansion_count = 0;
    
    for idx in range(len(players)):
        # 현재 플레이어
        now_players = players[idx]
        now_servers = server_count_list[idx]
        
        # 필요한 서버 산출
        server_needed = now_players // m
        
        # 현재의 서버 개수와 비교하고 부족하면 증설하는 로직
        if (server_needed > now_servers):
            expansion_count += server_needed - now_servers            
            print(f"{server_needed=}, {now_servers=}, {expansion_count=}")
            for ii in range(idx, min(idx + k, 24)):
                server_count_list[ii] += server_needed - now_servers 
        print(server_count_list)
        
    answer = 0
    
    return expansion_count