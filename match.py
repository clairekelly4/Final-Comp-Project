import numpy as np
from typing import List, Dict

# index ranges in the quiz responses
work_style_indices = [3, 4, 5, 6, 7]        # similar
leadership_indices = [8, 9, 10, 11, 12]     # diverse
coding_indices = [13, 14, 15, 16, 17]       # diverse

def get_difference(responses1: List[int], responses2: List[int], indices: List[int]) -> float:
    """
    calculates the absolute difference between two students' responses for a given set of quiz question indices
    :param responses1: first student's responses
    :param responses2: second student's responses
    :param indices: indices of the questions to compare
    :return: total difference for all questions
    """
    return sum(abs(responses1[i] - responses2[i]) for i in indices)
