'''
Created on Oct 16, 2015

@author: alkrinker
'''
from math import sqrt

def compute_pearson_correlation_coefficient(userAratings, userBratings):
    rating_a = 0
    rating_b = 0
    total = 0
    sum_a = 0
    sum_b = 0
    rating_product = 0
    sq_a = 0
    sq_b = 0
    for rating in userAratings:
        if rating in userBratings:
            rating_a = userAratings[rating]
            rating_b = userBratings[rating]
            total += 1
            rating_product += rating_a * rating_b
            sum_a += rating_a
            sum_b += rating_b
            sq_a += rating_a**2
            sq_b += rating_b**2
    if total == 0:
        return 0
    numerator = rating_product - (sum_a*sum_b/total)
    denominator = sqrt(sq_a - (sum_a**2)/total) * sqrt(sq_b - (sum_b**2)/total)
    if denominator == 0:
        return 0
    return numerator / denominator