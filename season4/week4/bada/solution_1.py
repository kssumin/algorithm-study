# 개인정보 수집 유효기간

import datetime
from dateutil.relativedelta import relativedelta

def solution(today, terms, privacies):
    answer = []
    
    today_dict = convert_date(today)
    today_date = datetime.date(today_dict["year"], today_dict["month"], today_dict["day"])
    
    term_dict = {}
    for term in terms:
        term_dict[term[0]] = int(term[2:])
    
    for i in range(len(privacies)):
        privacy_dict = convert_date(privacies[i][0:10])
        privacy_date = datetime.date(privacy_dict["year"], privacy_dict["month"], privacy_dict["day"])
        privacy_date += relativedelta(months=int(term_dict[privacies[i][11]]))

        if privacy_date.year < today_date.year:
            answer.append(i + 1)
        elif privacy_date.year == today_date.year:
            if privacy_date.month < today_date.month:
                answer.append(i + 1)
            elif privacy_date.month == today_date.month:
                if privacy_date.day <= today_date.day:
                    answer.append(i + 1)
            else:
                continue
                    
        else:
            continue
        
        
    return answer


def convert_date(date):
    date_dict = { "year": int(date[0:4]), "month": int(date[5:7]), "day": int(date[8:10])}
    
    return date_dict

'''
# 다른 사람의 풀이

def time_convert(t) :
    year, month, day = map(int, t.split('.'))
    return year * 12 * 28 + month * 28 + day

def solution(today, terms, privacies):
    term_dict = dict()
    today = time_convert(today)
    answer = []    
    
    for term in terms :
        name, period = term.split()
        term_dict[name] = int(period) * 28
    
    for idx, privacy in enumerate(privacies) :
        start, name = privacy.split()
        end = time_convert(start) + term_dict[name]
        if end <= today :
            answer.append(idx+1)    
    
    return answer
'''

'''
# 내 코드 리뷰

날짜를 숫자로 바꾸는 방법을 생각하지 못해서, 라이브러리를 사용했다.
라이브러리를 사용하는 것보다 날짜를 숫자로 바꾸는 함수를 직접 만드는 것이 더 좋은 코드가 될 것 같다.
'''