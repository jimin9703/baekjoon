def solution(clothes):
    answer = 1
    category = {}
    for value, key in clothes:
        if key in category.keys():
            category[key] += [value]
        else:
            category[key] = [value]
    print(category)
    for key, value in category.items():
        answer *= (len(value) + 1)
    return answer - 1