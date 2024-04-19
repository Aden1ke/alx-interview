#!/usr/bin/python3
"""
this module contains a function to determine if all the boxes can be opened.
"""

from typing import List, Set

def canUnlockAll(boxes):
    unlocked = [False] * len(boxes)
    # The first box is unlocked initially
    unlocked[0] = True
    # Start with the keys from the first box
    keys_stack = [0]

    while keys_stack:
        # Get the keys from the current box
        current_box = keys_stack.pop()
        for key in boxes[current_box]:
            if not unlocked[key]:
                unlocked[key] = True
                keys_stack.append(key)
    
    # Check if all boxes are unlocked
    return all(unlocked)
