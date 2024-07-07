#!/usr/bin/python3
"""Lockboxes module"""


def canUnlockAll(boxes):
    """
    determines if all the boxes can be opened
    return:
        True if all boxes can be opened, else return False
    """
    length = len(boxes)
    keys = set()
    opened_boxes = []
    i = 0

    while i < length:
        x = i
        opened_boxes.append(i)
        keys.update(boxes[i])
        for key in keys:
            if key != 0 and key < length and key not in opened_boxes:
                i = key
                break
        if x != i:
            continue
        else:
            break

    for i in range(length):
        if i not in opened_boxes and i != 0:
            return False
    return True
