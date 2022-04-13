def solution(a):
    seen = set()
    for v in a:
        if v in seen:
            return True
        else:
            seen.add(v)
    return False

a = [1,2,3]
print(solution(a) == False)
a.append(1)
print(solution(a) == True)