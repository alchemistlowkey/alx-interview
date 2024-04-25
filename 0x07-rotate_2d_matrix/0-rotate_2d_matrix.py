#!/usr/bin/python3
"""
Given an n x n 2D matrix, rotate it 90 degrees clockwise.

Prototype: def rotate_2d_matrix(matrix):
Do not return anything. The matrix must be edited in-place.
You can assume the matrix will have 2 dimensions and will not be empty.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in-place.

    Parameters:
    matrix (list of list): The 2D matrix to be rotated.

    Returns:
    None: The matrix is edited in-place.
    """

    n = len(matrix)

    # Iterate through each step of the matrix
    for step in range(n // 2):
        # Define the boundaries of the current step
        first = step
        last = n - 1 - step

        # Iterate through the elements in the current step
        for i in range(first, last):
            # Save the top element
            top = matrix[first][i]

            # Move left to top
            matrix[first][i] = matrix[last - (i - first)][first]

            # Move bottom to left
            matrix[last - (i - first)][first] = matrix[last][last -
                                                             (i - first)]

            # Move right to bottom
            matrix[last][last - (i - first)] = matrix[i][last]

            # Move top to right
            matrix[i][last] = top
