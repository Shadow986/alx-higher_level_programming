#!/usr/bin/python3
"""
This module contains a function that returns a list of lists of integers
representing the Pascal's triangle of n
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal's triangle of n

    Args:
        n (int): The number of rows of the triangle

    Returns:
        list: A list of lists of integers, each sublist representing a row of the triangle
    """
    if n <= 0:
        return []
    triangle = [[1]] # Initialize the triangle with the first row
    for i in range(1, n): # Loop from the second row to the nth row
        row = [1] # Start each row with 1
        for j in range(1, i): # Loop from the second element to the second last element of each row
            # The value of each element is the sum of the two elements above it
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1) # End each row with 1
        triangle.append(row) # Append each row to the triangle
    return triangle
