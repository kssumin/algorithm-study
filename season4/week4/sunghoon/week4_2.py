def solution(wallpaper):
    answer = [0, 0, 0, 0]
    for i in range(len(wallpaper)):
        if "#" in wallpaper[i]:
            answer[0] = i
            break

    for i in range(len(wallpaper) - 1, -1, -1):
        if "#" in wallpaper[i]:
            answer[2] = i + 1
            break

    a = len(wallpaper[0])
    for i in range(len(wallpaper)):
        c = wallpaper[i].find("#")
        if c == -1:
            continue
        a = min(a, c)

    answer[1] = a

    b = 0
    for i in range(len(wallpaper) - 1, -1, -1):
        d = wallpaper[i].rfind("#")

        b = max(b, d)

    answer[3] = b + 1
    return answer