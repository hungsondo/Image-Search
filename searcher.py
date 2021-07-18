# import the necessary packages
import numpy as np
import csv


class Searcher:
    def __init__(self, indexPath):
        # store our index path
        self.indexPath = indexPath

    def search(self, queryFeatures, limit=10):
        # initialize our dictionary of results
        results = {}
        # open the index file for reading
        with open(self.indexPath) as f:
            # Khởi tạo bộ đọc file CSV
            reader = csv.reader(f)
            # Vòng lặp từng dòng trong file index
            for row in reader:
                # Đọc image ID và features, rồi tính chi-squared distance giữa queryFeatures và features trong file index
                features = [float(x) for x in row[1:]]
                d = self.chi2_distance(features, queryFeatures)
                # now that we have the distance between the two feature
                # vectors, we can udpate the results dictionary -- the
                # key is the current image ID in the index and the
                # value is the distance we just computed, representing
                # how 'similar' the image in the index is to our query
                results[row[0]] = d
            # close the reader
            f.close()
        # sort our results, so that the smaller distances (i.e. the
        # more relevant images are at the front of the list)
        #Sắp xếp kết quả theo thứ tự tương đồng giảm dần
        results = sorted([(v, k) for (k, v) in results.items()])
        # trả về 10 results
        return results[:limit]

    def chi2_distance(self, histA, histB, eps=1e-10):
        # compute the chi-squared distance
        d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps)
                          for (a, b) in zip(histA, histB)])
        # return the chi-squared distance
        return d
