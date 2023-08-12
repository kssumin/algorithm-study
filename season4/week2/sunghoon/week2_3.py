def asd(a):
    b = []
    for i in a:
        if len(b) == 0:
            b.append(i)

        else:
            if i == ")" and b[-1] == "(":
                b.pop()
            elif i == "]" and b[-1] == "[":
                b.pop()
            elif i == "}" and b[-1] == "{":
                b.pop()
            else:
                b.append(i)

    if len(b) == 0:
        return 1
    else:
        return 0


def solution(s):
    answer = 0

    for _ in range(len(s)):
        if asd(s):
            answer += 1
        s = s[1:] + s[0]
    return answer