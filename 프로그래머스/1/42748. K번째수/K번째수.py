def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        li = sorted(array[commands[i][0]-1:commands[i][1]])
        answer.append(li[commands[i][2]-1])
    return answer