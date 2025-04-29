import numpy as np
from typing import List, Dict

# index ranges in the quiz responses
work_style_indices = [0, 1, 2, 3, 4]        # similar
leadership_indices = [5, 6, 7, 8, 9]     # diverse
coding_indices = [10, 11, 12, 13, 14]       # diverse

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
   :return: difference in diversity and similarity scores
   """
   # extract quiz responses for both students
   responses1, responses2 = student1['responses'], student2['responses']

   # measure similarity in work style (lower difference = more similar)
   similarity = get_difference(responses1, responses2, work_style_indices)

   # measure diversity in leadership and coding (higher difference = more diverse)
   diversity = get_difference(responses1, responses2, leadership_indices + coding_indices)

   # combine both metrics; prioritize diverse strengths but similar work styles
   return diversity - similarity # higher score = better

def match_students(students: List[Dict], group_size: int) -> List[List[str]]:
   """
   matches students into groups of a specified size based on their quiz responses
   - tries every pair of unmatched students
   - adds students one-by-one
   - calculates group scores
   - selects the best group in each round
   :param students: a list of student dictionaries with their name and responses
   :param group_size: a list of groups and each group is a list of student names
   :return: list of lists of ideal groupings of students
   """
   unmatched = students.copy() # students who have not been matched
   groups: List[List[str]] = []

   # runs as long as there are enough unmatched students to make a full group
   while len(unmatched) >= group_size:
       group = [unmatched.pop(0)] # start group with first unmatched

       while len(group) < group_size:
           best_student = None
           best_score = -np.inf

           for candidate in unmatched:
               # score candidate based on how well they fit with the current group
               score = sum(score_pair(candidate, member) for member in group)
               if score > best_score:
                   best_score = score
                   best_student = candidate

           group.append(best_student)
           unmatched.remove(best_student)

       groups.append([s["name"] for s in group])

       # handle any leftover students
       if unmatched:
           while len(unmatched) >= 2:  # make groups of 2 or more if possible
               group = [unmatched.pop(0)]
               while len(group) < group_size and unmatched:
                   best_student = None
                   best_score = -np.inf

                   for candidate in unmatched:
                       score = sum(score_pair(candidate, member) for member in group)
                       if score > best_score:
                           best_score = score
                           best_student = candidate

                   group.append(best_student)
                   unmatched.remove(best_student)

               groups.append([s["name"] for s in group])

           # if there is 1 student left, add them to the last group
           if unmatched:
               groups[-1].append(unmatched.pop(0)["name"])

       return groups