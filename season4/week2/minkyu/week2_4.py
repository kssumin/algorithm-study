def solution(cacheSize, cities):
    answer = 0
    user_data = []
    if cacheSize == 0:
        return len(cities) * 5

    for city in cities:
        city = city.upper()
        if city in user_data:
            answer += 1
            user_data.pop(user_data.index(city))
            user_data.append(city)
        else:
            answer += 5
            if len(user_data) < cacheSize:
                user_data.append(city)
            elif len(user_data) == cacheSize:
                user_data.pop(0)
                user_data.append(city)

    return answer