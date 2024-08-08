import sys

s = sys.stdin.readline().strip()

li = [-1] * 26

for i in range(len(s)):
    # 입력값의 글자의 아스키코드에서 a(시작)의 아스키코드를 뺀 값이 인덱스
    # 처음 입력 될때만 숫자 대입하고 이미 입력되어 있을 때는 넘어감
    if li[ord(s[i]) - ord('a')] == -1:
        li[ord(s[i]) - ord('a')] = i

print(*li)