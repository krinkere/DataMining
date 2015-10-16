'''
Created on Oct 16, 2015

@author: alkrinker
'''
from RecommendationSystem import recommender_via_pearson
from Test import user_music_ratings
import unittest

class TestRecommenderViaPearson(unittest.TestCase):
 
    def setUp(self):
        self.ratings = user_music_ratings.ratings

    def test_compute_pearson_correlation_coefficient_Angelica_Bill(self):
        result = recommender_via_pearson.compute_pearson_correlation_coefficient(self.ratings['Angelica'], self.ratings['Bill'])
        self.assertEqual(-0.9040534990682699, result)

    def test_compute_pearson_correlation_coefficient_Angelica_Hailey(self):
        result = recommender_via_pearson.compute_pearson_correlation_coefficient(self.ratings['Angelica'], self.ratings['Hailey'])
        self.assertEqual(0.420084025208, result)

    def test_compute_pearson_correlation_coefficient_Angelica_Jordyn(self):
        result = recommender_via_pearson.compute_pearson_correlation_coefficient(self.ratings['Angelica'], self.ratings['Jordyn'])
        self.assertEqual(0.763974860548, result)
