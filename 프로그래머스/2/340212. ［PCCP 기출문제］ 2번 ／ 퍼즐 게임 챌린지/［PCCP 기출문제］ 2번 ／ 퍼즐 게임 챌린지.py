'''
퍼즐을 푸는데 걸리는 시간
* diff <= level : time_cur
* diff > level : (diff - level) * (time_cur + time_prev) + time_cur

limit 안에서 최솟값 -> 이진 탐색
'''
def solution(diffs: list, times: list, limit: int) -> int:
    left, right = min(diffs), max(diffs)
    while left < right:
        mid = (left + right) // 2
        used_time = 0
        
        for i, diff in enumerate(diffs):
            if diff <= mid:
                used_time += times[i]
            else:
                time_prev = 0 if i == 0 else times[i - 1]
                used_time += (diff - mid) * (times[i] + time_prev) + times[i]
        print(used_time)
        if used_time > limit:
            left = mid + 1
        else:
            right = mid
    
    return left