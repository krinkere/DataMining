'''
Created on Oct 27, 2015

@author: alkrinker
'''
import random

def divide_into_buckets(filename, bucketName, separator, classColumn):
    """the original data is in the file named filename
    bucketName is the prefix for all the bucket names
    separator is the character that divides the columns (for ex., a tab or comma)
    classColumn is the column that indicates the class"""

    # Number of buckets
    numberOfBuckets = 10
    data = {}

    # Read in the data and divide by category
    with open(filename) as f:
        lines = f.readlines()
    for line in lines:
        if separator != '\t':
            line = line.replace(separator, '\t')
        # Get the category
        category = line.split('\t')[classColumn]
        data.setdefault(category, [])
        data[category].append(line)
    # Initialize the buckets
    buckets = []
    for i in range(numberOfBuckets):
        print "Creating %d " % i
        buckets.append([])
    # Based on category put data in a bucket
    for k in data.keys():
        print data[k]
        random.shuffle(data[k])
        print data[k]
        bNum = 0
        # Divide into buckets
        for item in data[k]:
            buckets[bNum].append(item)
            bNum = (bNum + 1) % numberOfBuckets
    # Write to a file
    for j in range(numberOfBuckets):
        f = open("data/%s-%03i" % (bucketName, j+1), 'w')
        for item in buckets[j]:
            f.write(item)
        f.close()
