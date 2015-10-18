'''
Created on Oct 16, 2015

@author: alkrinker

If your data is dense (almost all attributes have non-zero values) and the magnitude of the attribute values
is important, use distance measures such as Euclidean or Manhattan. Manhattan is faster.
Minkowski with coefficient 1 => Manhattan
Minkowski with coefficient 2 => Euclidean
'''
from RecommendationSystem import recommender_commons

def compute_manhattan_distance(userAratings, userBratings):
    """Computes the Manhattan distance. 
    Both userAratings and userBratings are dictionaries
       of the form {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}"""
    distance = 0
    for rating in userAratings:
        if rating in userBratings:
            distance += abs(userAratings[rating] - userBratings[rating])
    return distance

def compute_minkowski_score(userAratings, userBratings, coefficient):
    """Return inverted value of minkowski value. Since Minkowski returns distance, the less 
    distance, more similar they are, the distance is less, hence the score is bigger. 
    Add 1 so that we won't be dividing by zero."""
    return 1 / (1 + compute_minkowski_distance(userAratings, userBratings, coefficient))

def compute_minkowski_distance(userAratings, userBratings, coefficient=1):
    """Computes the Minkowski distance. 
    For coefficient = 1 , coefficient = 2, the Minkowski metric becomes equal to the 
        Manhattan and Euclidean metrics respectively.
    Both userAratings and userBratings are dictionaries 
       of the form {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}"""
    distance = 0
    calculate = False
    for rating in userAratings:
        if rating in userBratings:
            distance += pow(abs(userAratings[rating] - userBratings[rating]),coefficient)
            calculate = True
    if calculate:
        if distance == 0: # Indicates possible same person!
            return 0
        return pow(distance, 1/coefficient)
    else:
        return 0 # Indicates no ratings in common

def recommend(user_in_question, users, coefficient):
    return recommender_commons.recommend(user_in_question, users, compute_minkowski_distance, coefficient)

