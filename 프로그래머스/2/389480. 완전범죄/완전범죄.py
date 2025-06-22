'''
1. info 정렬 (첫 번째 인덱스 높은순, 두 번째 인덱스 낮은순) -> nlogn
2. 앞에서부터 도둑이 가능한만큼 훔치기 -> n
'''
def solution(info: list, n: int, m: int) -> int:
    answer = [0, 0]
    
    info.sort(key=lambda x: (x[1] - x[0], -x[0]))
    
    for a, b in info:
        if answer[1] + b < m:
            answer[1] += b
        elif answer[0] + a < n:
            answer[0] += a
        else:
            return -1
            
    return answer[0]