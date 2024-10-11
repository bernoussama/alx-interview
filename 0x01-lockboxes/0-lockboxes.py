#!/usr/bin/python3
"""
can all boxes be unlocked ?
"""


def canUnlockAll(boxes):
    """
    can all boxes be unlocked ?
    """
    n = len(boxes)
    # list keeping track of unlocked boxes
    unlocked = [False] * n
    unlocked[0] = True

    queue = [0]
    while queue:
        current = queue.pop(0)

        for key in boxes[current]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                queue.append(key)

    return all(unlocked)
