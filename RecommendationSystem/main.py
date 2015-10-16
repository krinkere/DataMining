'''
Created on Oct 16, 2015

@author: alkrinker
'''
from RecommendationSystem import recommender_via_pearson
from RecommendationSystem import recommender_via_minkowski

users = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bill":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
         "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
         "Jordyn":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
        }

print recommender_via_pearson.compute_pearson_correlation_coefficient(users['Angelica'], users['Bill'])
print recommender_via_pearson.compute_pearson_correlation_coefficient(users['Angelica'], users['Hailey'])
print recommender_via_pearson.compute_pearson_correlation_coefficient(users['Angelica'], users['Jordyn'])

user_in_question = "Angelica"
results = recommender_via_minkowski.recommend(user_in_question, users)
print "List of movies that %s might like based on most similar user %s taste: %r" \
    % (user_in_question, results[0], results[1])
"""
print "Difference between Bill and Sam"
print compute_manhattan_distance(users["Bill"], users["Sam"])
print "Difference between Hailey and Jordyn"
print compute_manhattan_distance(users['Hailey'], users['Jordyn'])
print "List people similar to Sam in his taste"
print find_similar_users("Sam", users)
print "List people similar to Hailey in his taste"
print find_similar_users("Hailey", users)
"""