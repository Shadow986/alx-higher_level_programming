#!/usr/bin/python3
"""
This module contains the function lazy_matrix_mul which multiplies two matrices using NumPy.
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    This function multiplies two matrices using NumPy.
    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.
    Returns:
        numpy.ndarray: The product of the two matrices.
    Raises:
        TypeError: If m_a or m_b is not a list, not a list of lists, contains non-integers/floats, or is not rectangular.
        ValueError: If m_a or m_b is empty or if m_a and m_b cannot be multiplied.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]] or m_b == [] or m_b == [[]]:
        raise ValueError("m_a can't be empty" if m_a == [] or m_a == [[]] else "m_b can't be empty")
    if not all(isinstance(el, (int, float)) for row in m_a for el in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(el, (int, float)) for row in m_b for el in row):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    try:
        return np.matmul(m_a, m_b)
    except ValueError:
        raise ValueError("m_a and m_b can't be multiplied")
