import kNN
from numpy import *
import matplotlib
import matplotlib.pyplot as plt

print kNN.classify0([0, 0], array([[1, 0], [2, 1]]), ['A', 'B'], 1)

datingDataMat, datingLabels = kNN.file2matrix('test2.txt')
# datingDataMat = numpy.zeros((3,3))
# datingDataMat[2,:] = [2,1,0]
# datingLabels = numpy.zeros((3,3))
# datingLabels[2,:] = [2,1,0]
# print datingDataMat , datingLabels
# color = 30.0 * numpy.array(datingLabels)
# print color
datingLabels = array(datingLabels) + 3

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:, 0], datingDataMat[:, 1], 20 * array(datingLabels), 20 * array(datingLabels))
plt.show()


# ax.scatter([2,3,1],[3,1,2])
