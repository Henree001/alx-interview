#!/usr/bin/python3
'''A module for working with lockboxes.
'''


def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
    '''
    box_length = set(range(1, len(boxes)))
    # print(len(box_length))

    for index, box in enumerate(boxes):
        if index == len(boxes) - 2 and len(box_length) != 0:
            if not box_length.issubset(box):
                break

        for index, key in enumerate(box):
            if key in box_length:
                box_length.remove(key)

    return len(box_length) == 0
