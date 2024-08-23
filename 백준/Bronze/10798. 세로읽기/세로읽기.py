import sys

li_word = []

for i in range(5):
    li = [""] * 15
    word = sys.stdin.readline().strip()
    for j in range(len(li)):
        if j < len(word):
            li[j] = word[j]
            
        else:
            pass
        
    li_word.append(li)

for i in range(15):
    for j in range(5):
        print(li_word[j][i], end="")