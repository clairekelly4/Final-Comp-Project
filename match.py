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

def score_pair(student1: Dict, student2: Dict) -> float:
   """
   gives a score to a pair of students by measuring how similar they are in work style and how different they are in leadership and coding
   then subtracts similarity from diversity -> higher score = better match
   :param student1: first student
   :param student2: second student
   :return:
   """
   # extract quiz responses for both students
   responses1, responses2 = student1['responses'], student2['responses']

   # measure similarity in work style (lower difference = more similar)
   similarity = get_difference(responses1, responses2, work_style_indices)

   # measure diversity in leadership and coding (higher difference = more diverse)
   diversity = get_difference(responses1, responses2, leadership_indices + coding_indices)

   # combine both metrics; prioritize diverse strengths but similar work styles
   return diversity - similarity # higher score = better

