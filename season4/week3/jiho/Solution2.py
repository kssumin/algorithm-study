def solution(weights):
    answer = 0
    
    a = {}
    
    for i in weights:
        if i in a:
            a[i] += 1
        else:
            a[i] = 1
            
    for i in a:
        if a[i] > 1:
            answer += (a[i] * (a[i]-1)) / 2
        if i*2 in a:
            answer += a[i] * a[2*i]
        if i*2/3 in a:
            answer += a[i] * a[i*2/3]
        if i*3/4 in a:
            answer += a[i] * a[i*3/4]

    return answer
            
