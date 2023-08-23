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

    for box in boxes:
        for index, key in enumerate(box):
            if index == len(box) - 2 and key != len(box_length):
                break
            if key in box_length:
                box_length.remove(key)
                print(box_length)

    return len(box_length) == 0
