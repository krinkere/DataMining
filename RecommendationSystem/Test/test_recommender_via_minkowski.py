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
        results = recommender_via_minkowski.recommend(user_in_question, ratings)
        print "List of movies that %s might like based on most similar user %s taste: %r" \
            % (user_in_question, results[0], results[1])
        self.assertEqual('Chan', results[0])
        self.assertEqual('Deadmau5', results[1][0][0])
        self.assertEqual(1.0, results[1][0][1])