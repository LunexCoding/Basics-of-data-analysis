import pandas as pd

#Series
dataDictForSeries = {'a': 1, 'b': 2, 'c': 3}
newSeriesFromDict = pd.Series(data=dataDictForSeries, index=['a', 'b', 'c'])
print(newSeriesFromDict, '\n')

dataListForSeries = [3, 5, 7]
newSeriesFromList = pd.Series(dataListForSeries, copy=False)
print(newSeriesFromList, '\n')

#DataFrame
dataDictForFrame = {'col1': [1, 2], 'col2': [3, 4]}
newFrameFromDict = pd.DataFrame(data=dataDictForFrame)
print(newFrameFromDict, '\n')

dataListForFrame = [(3, 5, 7), (5, 8, 1)]
newFrameFromList = pd.DataFrame(data=dataListForFrame, columns=['col1', 'col2', 'col3'])
print(newFrameFromList, '\n')

#index
indexDict = pd.Index({'col1': [1, 2], 'col2': [3, 4]})
print(indexDict, '\n')

indexList = pd.Index([5, 2, 3])
print(indexList, '\n')

#selecting
newSeriesFromDictTwo = pd.Series(dataDictForSeries, index=list('abc'))
print(newSeriesFromDictTwo.a)
