'''
Created on Oct 27, 2015

@author: alkrinker
'''
import unittest
import os
from Utils import divide_into_buckets

class TestUtils(unittest.TestCase):
    """Split big file into 10... will need it for 10 Fold Validation"""
    def test_divide_into_buckets(self):
        """Clean data directory"""
        folder = 'data'
        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
            except Exception, e:
                print e
        
        """Done cleaning"""
        divide_into_buckets("../../Data/mpgData.txt", 'mpgData','\t',0)
        """Check that file was created"""
        generated_file = "data/mpgData-001"
        print os.path.exists(generated_file)
        