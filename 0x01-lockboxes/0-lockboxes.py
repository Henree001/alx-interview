#!/usr/bin/python3
'''A module for working with lockboxes.
'''


def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
    '''
    box_keys = set(range(1, len(boxes)))

    for index, box in enumerate(boxes):
        #     if index == len(boxes) - 2 and len(box_keys) != 0:
        #         if not box_keys.issubset(box):
        #             break

        for key in box:
            if key == index:
                continue
            if key in box_keys:
                box_keys.remove(key)

    return len(box_keys) == 0
