def solution(s):
    words = s.split()
    answer = []
    for word in words:
        new_word = ""
        for i in range(len(word)):
            if i % 2 == 0:
                new_word += word[i].upper()
            else:
                new_word += word[i].lower()
        answer.append(new_word)

    return ' '.join(answer)