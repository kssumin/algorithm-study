def solution(phone_number):
    answer = ''
    four = phone_number[-4:]
    answer = "*" * (len(phone_number) - 4)

    return answer + four