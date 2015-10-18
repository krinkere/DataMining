'''
Created on Oct 18, 2015

@author: alkrinker
'''
def find_similar_users(user_in_question, users, distance_method, coefficient):
    """Creates sorted list of users that are similar in their taste to the user in question"""
    similars = []
    for user in users:
        if user != user_in_question:
            if (coefficient > 0):
                similar_rating = distance_method(users[user_in_question], users[user], coefficient)
            else:
                similar_rating = distance_method(users[user_in_question], users[user])
            similars.append((similar_rating, user))
    # Now sort based on similar_rating
    similars.sort()
    if coefficient == -1:
        similars.reverse()
    print "Similar users to %s: %r" % (user_in_question, similars)
    return similars

def find_user_with_same_taste(user_in_question, users, distance_method, coefficient=1):
    return find_similar_users(user_in_question, users, distance_method, coefficient)[0][1]

def recommend(user_in_question, users, distance_method, coefficient):
    """Return recommendations for given user in question"""
    # find most user with close taste 
    similar_user = find_user_with_same_taste(user_in_question, users, distance_method, coefficient)
    print "Most similar user %s" % similar_user
    
    # Find unrates for user_in_question
    unrates = []
    similar_user_ratings = users[similar_user]
    print "Similar user %s likes %r" % (similar_user, similar_user_ratings)
    user_in_question_ratings = users[user_in_question]
    print "User in question %s likes %r" % (user_in_question, user_in_question_ratings)
    
    for band in similar_user_ratings:
        if not band in user_in_question_ratings: 
            unrates.append((band, similar_user_ratings[band]))
    return similar_user, sorted(unrates, key=lambda bandTuple: bandTuple[1], reverse=True)