import logRegres

dataArr, labelMat = logRegres.loadDataSet()
wei = logRegres.gradAscend(dataArr, labelMat)
logRegres.plotBestFit(wei)