#!/usr/bin/python3
"""
Question:
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.
Write a method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
    - boxes (list of lists): Each box contains keys to other boxes.

    Returns:
    - bool: True if all boxes can be opened, else False.
    """

    # A set to keep track of the opened boxes
    opened = {0}  # Initialize with d 1st box (index 0) which is already opened

    # List to keep track of the boxes to explore
    to_explore_boxes = [0]  # Start exploration from the first box

    # Iterate through the boxes to explore
    for next_box in to_explore_boxes:
        # Check keys in the current box
        for next_box_key in boxes[next_box]:
            # If the key opens a new box and that box hasn't been opened yet
            if next_box_key < len(boxes) and next_box_key not in opened:
                # Mark the box as opened
                opened.add(next_box_key)
                # Add the newly opened box to the list of boxes to explore
                to_explore_boxes.append(next_box_key)

    # Check if all boxes are opened
    return len(opened) == len(boxes)
