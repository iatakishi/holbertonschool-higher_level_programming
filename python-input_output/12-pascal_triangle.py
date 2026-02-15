#!/usr/bin/python3
"""Returns Pascal's triangle of n rows."""


def pascal_triangle(n):
    """This function outputs pascal triangle."""
    if n <= 0:
        return []

    triangle = [[1]]  # first row

    for i in range(1, n):
        prev = triangle[-1]
        row = [1]  # start with 1

        for j in range(1, len(prev)):
            row.append(prev[j - 1] + prev[j])  # sum of two parents

        row.append(1)  # end with 1
        triangle.append(row)

    return triangle
