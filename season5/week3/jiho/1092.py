import sys

read = sys.stdin.readline

N = int(read())
cranes = list(map(int, read().split()))

M = int(read())
boxes = list(map(int, read().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

if boxes[0] > cranes[0]:
    print(-1)
    sys.exit()
else:
    time = 0

    while boxes:
        if not boxes:
            break

        for crane in cranes:
            for box in boxes:
                if crane >= box:
                    boxes.remove(box)
                    break

        time += 1

    print(time)