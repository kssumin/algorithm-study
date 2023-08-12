def solution(s):
    count, zero = 0, 0
    answer = []

    while True:
        if s == "1":
            break

        else:
            zero += s.count("0")
            s = s.replace("0", "")

            s = bin(len(s))[2:]

            count += 1

    answer = [count, zero]
    return answer