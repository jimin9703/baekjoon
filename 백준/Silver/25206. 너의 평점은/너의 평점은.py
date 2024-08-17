import sys

score = [sys.stdin.readline().strip().split() for _ in range(20)]
dict_s = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0": 1.0, "F":0.0}
sum_s = 0
cnt = 0 

for i in range(20):
    if score[i][2] == "P":
        pass
    else:
        sum_s += float(score[i][1]) * dict_s[score[i][2]]
        cnt += float(score[i][1])

print(sum_s / cnt)