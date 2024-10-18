import heapq
def solution(scoville, K):
    answer = 0
    ans = []
    cnt = 0
    for i in range(len(scoville)):
        heapq.heappush(ans, scoville[i])
    
    while len(ans) > 1:
        min1 = heapq.heappop(ans)
        if min1 >= K:
            return cnt
        min2 = heapq.heappop(ans)
        
        new = min1+(min2*2)
        heapq.heappush(ans, new)
        cnt += 1
    if ans[0] >= K:
        return cnt
    else:
        return -1