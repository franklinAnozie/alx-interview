#!/usr/bin/python3
""" lockboxes algo """


def canUnlockAll(boxes):
    n = len(boxes)
    opened = []
    keys = [0]

    while keys:
        current_key = keys.pop()
        if current_key not in opened:
            opened.append(current_key)
            for key in boxes[current_key]:
                if key not in keys and key not in opened:
                    keys.append(key)

    return len(opened) == n
