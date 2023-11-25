def solution(phone_number):
    answer = ''
    star_len = len(phone_number) - 4
    return star_len * '*' + phone_number[-4:]