def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    
    for i in range(len(citations)):
        if i >= citations[i]:
            return i
            
    return len(citations)