from collections import deque

def solution(players, m, k):
    answer = 0
    server, server_cnt = deque(), 0
    
    for i in range(24):
        while server and server[0][0] < i:
            server_cnt -= server.popleft()[1]
        
        n = players[i] // m - server_cnt
        if n > 0:
            server.append((i + k - 1, n))
            server_cnt += n
            answer += n
    
    return answer