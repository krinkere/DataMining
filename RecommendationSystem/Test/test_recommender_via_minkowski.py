'''
Created on Oct 16, 2015

@author: alkrinker
'''
from Test import user_music_ratings
import unittest

from RecommendationSystem import recommender_via_minkowski
from Test.user_music_ratings import ratings

class TestRecommenderViaMinkowski(unittest.TestCase):
 
    def setUp(self):
        self.ratings = user_music_ratings.ratings

    def test_recommender_via_minkowski(self):
        user_in_question = "Sam"
        results = recommender_via_minkowski.recommend(user_in_question, ratings, 1)
        print "List of movies that %s might like based on most similar user %s taste: %r" \
            % (user_in_question, results[0], results[1])
        self.assertEqual('Al', results[0])
        self.assertEqual('Deadmau5', results[1][0][0])
        self.assertEqual(5.0, results[1][0][1])

    def test_same_user_rating(self):
        user_in_question = "Sam"
        distance = recommender_via_minkowski.compute_minkowski_distance(self.ratings[user_in_question], self.ratings[user_in_question], 2)
        # Same person. hence score of 1 and distance is 0
        self.assertEqual(0.0, distance)
        score = recommender_via_minkowski.compute_minkowski_score(self.ratings[user_in_question], self.ratings[user_in_question], 2)
        self.assertEqual(1.0, score)

    def test_recommender_via_minkowski_for_al(self):
        user_in_question = "Al"
        results = recommender_via_minkowski.recommend(user_in_question, ratings, 1)
        print "List of movies that %s might like based on most similar user %s taste: %r" \
            % (user_in_question, results[0], results[1])
        self.assertEqual('Angelica', results[0])
