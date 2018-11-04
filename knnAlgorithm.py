import collections as col
import scipy.spatial.distance as sd


class knnAlgorithm:
    def __init__(self, length, data):
        self.k = length
        self.learningData = data
	    self.labels = []
		self.resultlist = []
		self.distancelist = []
	    self.count = 0

    def getlabel(self, neighborlist):
        for i in range(len(neighborlist)):
            labels.append(neighborlist[i][4])
        counter = col.Counter(labels)
        return counter.most_common(1)[0][0]

    def predict(self, testdata):
        for i in range(len(testdata)):
            for j in range(len(self.learningData)):
                dist = sd.euclidean(testdata[i][0:4], self.learningData[j][0:4])
                distancelist.append((self.learningData[j], dist))
            distancelist.sort(key=lambda x: x[1])
            neighbors = []
            for x in range(self.k):
                neighbors.append(distancelist[x][0])
            resultlist.append(self.getlabel(neighbors))
        return resultlist

    def score(self, testdata, resultlist):
        for i in range(len(testdata)):
            if(testdata[i][4]==resultlist[i]):
                count=count+1
        return  float(count)/len(testdata)