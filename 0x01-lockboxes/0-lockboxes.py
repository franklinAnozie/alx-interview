#!/usr/bin/python3
""" lockboxes algo """

def canUnlockAll(boxes=[[]]):
    if all(type(box) == list for box in boxes):
        opened = [0]
        for num in range(len(boxes)):
            closed = boxes[num]
            while len(closed) > 0:
                key = closed.pop()
                if key not in opened:
                    opened.append(key)
        print(opened)
    else:
        return False

if __name__ == "__main__":
    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    canUnlockAll(boxes)
