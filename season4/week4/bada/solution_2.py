def solution(wallpaper):
    answer = []
    
    w = len(wallpaper[0])
    h = len(wallpaper)
    
    folder_w = []
    folder_h = []
    
    for i in range(h):
        for j in range(w):
            if wallpaper[i][j] == "#":
                folder_w.append(j)
                folder_h.append(i)
                
    print(folder_w)
    print(folder_h)
                
    folder_w.sort()
    folder_h.sort()
    
                
    answer.append(folder_h[0])
    answer.append(folder_w[0])
    answer.append(folder_h[-1] + 1)
    answer.append(folder_w[-1] + 1)
            
            
    
    return answer

'''
정사각형 격자판
상태 문자열 배열 wallpaper
각 #들의 x좌표와 y좌표를 구하고
x들 중 최소, 최대 / y들 중 최소, 최대 찾기
'''