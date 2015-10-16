'''
Created on Oct 16, 2015

@author: alkrinker
'''
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

def compute_minkowski_distance(userAratings, userBratings, coefficient):
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
    
def find_similar_users(user_in_question, users):
    """Creates sorted list of users that are similar in their taste to the user in question"""
    similars = []
    for user in users:
        if user != user_in_question:
            similar_rating = compute_minkowski_distance(users[user_in_question], users[user], 1)
            similars.append((similar_rating, user))
    # Now sort based on similar_rating
    similars.sort()
    print "Similar users to %s: %r" % (user_in_question, similars)
    return similars

def find_user_with_same_taste(user_in_question, users):
    return find_similar_users(user_in_question, users)[0][1]

def recommend(user_in_question, users):
    """Return recommendations for given user in question"""
    # find most user with close taste 
    similar_user = find_user_with_same_taste(user_in_question, users)
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

