'''
Created on Nov 8, 2015

@author: alkrinker
'''
import copy

class Classifier:
    def __init__(self, bucketPrefix, testBucketNumber, dataFormat):
        """
            Given file pattern 'bucketPrefix', specify test file 'tstBucketNumber'
            'dataFormat' provides how to interpret tab delimited data, such as
            class    num    num    num    num    num    comment
        """
        self.medianAndDeviation=[]
        
        # read the data in from the file
        self.format = dataFormat.strip().split('\t')
        self.data = []
        # iterate through buckets. Since it is 10 fold validation we will have
        # 10 of them.
        for i in range(1,11):
            # if it is a testBucketNumber then skip it. Otherwise proceed
            if i != testBucketNumber:
                filename = "%s-%03i" % (bucketPrefix, i)
                f = open(filename)
                lines = f.readlines()
                f.close()
                for line in lines:
                    fields = line.strip().split('\t')
                    ignore = []
                    vector = []
                    for j in range(len(fields)):
                        if self.format[j] == 'num':
                            vector.append(float(fields[j]))
                        elif self.format[j] == 'comment':
                            '''??? - Why to keep ignored elements?'''
                            ignore.append(fields[j])
                        elif self.format[j] == 'class':
                            '''??? - scope? this will be available even outside of this loop? '''
                            classification = fields[j]
                    '''??? - Why we need double (())'''
                    self.data.append((classification, vector, ignore))
        self.rawData = copy.deepcopy(self.data)
        # get length of instance vector
        self.vlen = len(self.data[0][1])
        # now normalize the data
        for i in range(self.vlen):
            self.normalizeColumn(i)
            
    def normalizeColumn(self, columnNumber):
        """given a column number, normalize that column in self.data"""
        # first extract values to list
        '''??? - what is v[1][columnNumber]'''
        col = [v[1][columnNumber] for v in self.data]
        median = self.getMedian(col)
        asd = self.getAbsoluteStandardDeviation(col, median)
        print("Median: %f   ASD = %f" % (median, asd))
        self.medianAndDeviation.append((median, asd))
        for v in self.data:
            v[1][columnNumber] = (v[1][columnNumber] - median) / asd

    def getMedian(self, alist):
        """
        return median of alist
        """
        if alist == []:
            return []
        blist = sorted(alist)
        length = len(alist)
        if length % 2 == 1:
            # length of list is odd so return middle element
            return blist[int(((length + 1) / 2) - 1)]
        else:
            # length of list is even so compute midpoint
            v1 = blist[int(length / 2)]
            v2 = blist[(int(length / 2) - 1)]
            return (v1 + v2) / 2.0

    def getAbsoluteStandardDeviation(self, alist, median):
        """
        given alist and median return absolute standard deviation
        """
        total_sum = 0
        for item in alist:
            total_sum += abs(item - median)
        return total_sum / len(alist)
    
    def classify(self, itemVector):
        """
        Return class we think item Vector is in
        """
        return(self.nearestNeighbor(self.normalizeVector(itemVector))[1][0])
    
    def nearestNeighbor(self, itemVector):
        """
        return nearest neighbor to itemVector
        """
        return min([ (self.manhattan(itemVector, item[1]), item)
                     for item in self.data])
        
    def manhattan(self, vector1, vector2):
        """
        Computes the Manhattan distance.
        """
        return sum(map(lambda v1, v2: abs(v1 - v2), vector1, vector2))
    
    def normalizeVector(self, v):
        """
        We have stored the median and asd for each column.
        We now use them to normalize vector v
        """
        vector = list(v)
        for i in range(len(vector)):
            (median, asd) = self.medianAndDeviation[i]
            vector[i] = (vector[i] - median) / asd
        return vector
    
    def testBucket(self, bucketPrefix, bucketNumber):
        """
        test classified with ten fold validation
        """

        #path = "data/"

        filename = "%s-%03i" % (bucketPrefix, bucketNumber)
        f = open (filename)
        lines = f.readlines()
        f.close()

        totals = {}
        for line in lines:
            data = line.strip().split('\t')
            vector = []
            classInColumn = -1
            for i in range(len(self.format)):
                if self.format[i] == 'num':
                    vector.append(float(data[i]))
                elif self.format[i] == 'class':
                    classInColumn = i
            theRealClass = data[classInColumn]
            classifiedAs = self.classify(vector)
            totals.setdefault(theRealClass,{})
            totals[theRealClass].setdefault(classifiedAs, 0)
            totals[theRealClass][classifiedAs] += 1
        
        return totals

def tenfold(bucketPrefix, dataFormat):
    results = {}
    for i in range(1,11):
        c = Classifier(bucketPrefix, i, dataFormat)
        t = c.testBucket(bucketPrefix, i)
        for (key, value) in t.items():
            results.setdefault(key, {})
            for (ckey, cvalue) in value.items():
                results[key].setdefault(ckey, 0)
                results[key][ckey] += cvalue
                
    # print results
    categories = list(results.keys())
    categories.sort()
    print ("\n Classified as: ")
    print(   "\n       Classified as: ")
    header =    "        "
    subheader = "      +"
    for category in categories:
        header += category + "   "
        subheader += "----+"
    print (header)
    print (subheader)
    total = 0.0
    correct = 0.0
    for category in categories:
        row = category + "    |"
        for c2 in categories:
            if c2 in results[category]:
                count = results[category][c2]
            else:
                count = 0
            row += " %2i |" % count
            total += count
            if c2 == category:
                correct += count
        print(row)
    print(subheader)
    print("\n%5.3f percent correct" %((correct * 100) / total))
    print("total of %i instances" % total)

tenfold("../Test/data/mpgData", "class\tnum\tnum\tnum\tnum\tnum\tcomment")