from collections import defaultdict


def solution(edges: list) -> list:
    answer = [0, 0, 0, 0]
    nodes = set()
    graph = defaultdict(list)
    incoming_egde, outgoing_egde = defaultdict(int), defaultdict(int)
    
    for a, b in edges:
        graph[a].append(b)
        incoming_egde[b] += 1
        outgoing_egde[a] += 1
        nodes.add(a)
        nodes.add(b)
        
    for node in nodes:
        if outgoing_egde[node] > 1 and incoming_egde[node] == 0:
            answer[0] = node
            for i in graph[node]:
                incoming_egde[i] -= 1
            break
            
    for node in nodes:
        if node == answer[0]:
            continue
        if incoming_egde[node] == 0:
            answer[2] += 1
        if incoming_egde[node] > 1 and outgoing_egde[node] > 1:
            answer[3] += 1
    
    answer[1] = len(graph[answer[0]]) - answer[2] - answer[3]
    
    return answer