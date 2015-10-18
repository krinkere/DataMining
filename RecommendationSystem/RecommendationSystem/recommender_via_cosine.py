'''
Created on Oct 17, 2015

@author: alkrinker

If the data is sparse consider using Cosine Similarity
'''
from math import sqrt
from RecommendationSystem import recommender_commons

def compute_cosine_similarity(userAratings, userBratings):
    """Computes the Cosine similarity
    cos(x,y) = x*y/||x||x||y||"""
    sum_of_sqr_x = 0
    sum_of_sqr_y = 0
    dot_product = 0
    for rating in userAratings:
        sum_of_sqr_x += pow(userAratings[rating],2)
        if rating in userBratings:
            dot_product += userAratings[rating] * userBratings[rating]

    for rating in userBratings:
        sum_of_sqr_y += pow(userBratings[rating],2)
        
    sqrt_of_sum_of_sqr_x = sqrt(sum_of_sqr_x)
    sqrt_of_sum_of_sqr_y = sqrt(sum_of_sqr_y)
    
    denominator = sqrt_of_sum_of_sqr_x * sqrt_of_sum_of_sqr_y
    
    if denominator == 0:
        return 0
    else:
        return dot_product / denominator

def recommend(user_in_question, users):
    return recommender_commons.recommend(user_in_question, users, compute_cosine_similarity, -1)
