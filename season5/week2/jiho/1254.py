import sys

sentence = str(sys.stdin.readline().strip())
for i in range(len(sentence)):
    if sentence[i:] == sentence[i:][::-1]:
        print(len(sentence)+i)
        break
