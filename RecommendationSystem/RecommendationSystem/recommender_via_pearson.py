'''
Created on Oct 16, 2015

@author: alkrinker

If the data is subject to grade-inflation(different users maybe using different scales) use Pearson
'''
from math import sqrt

def compute_pearson_correlation_coefficient(userAratings, userBratings):
    """ Returns score between -1 and 1. 1 being most similar """
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

def find_similar_users(user_in_question, users):
    """Creates sorted list of users that are similar in their taste to the user in question via Pearson coefficient"""
    person_coefficients = []
    for user in users:
        if user != user_in_question:
            person_coefficient = compute_pearson_correlation_coefficient(users[user_in_question], users[user])
            person_coefficients.append((person_coefficient, user))
    # Now sort based on similar_rating
    person_coefficients.sort()
    print "Similar users to %s: %r" % (user_in_question, person_coefficients)
    return person_coefficients

def recommend(user_in_question, users):
    totals = {}
    simSum = {}
    for user in users:
        if user != user_in_question:
            person_coefficient = compute_pearson_correlation_coefficient(users[user_in_question], users[user])

            # ignore anyone who scores less than zero since their tastes are not similiar
            if person_coefficient <= 0:
                continue
            for rating in users[user]:
                if rating not in users[user_in_question]:
                    score = users[user][rating] * person_coefficient
                    totals.setdefault(rating, 0)
                    totals[rating] += score
                    simSum.setdefault(rating, 0)
                    simSum[rating] += person_coefficient

    rankings = [(total/simSum[rating], rating) for rating,total in totals.items()]
    rankings.sort()
    rankings.reverse()
    # Return recommended list
    recommendations = [recommend_item for score,recommend_item in rankings]
    return recommendations