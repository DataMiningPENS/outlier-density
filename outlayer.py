from scipy.spatial import distance
from sklearn import cluster as skcluster
from collections import defaultdict

# *** INITIALIZATION DATA ***
data = []
data.append([80,60,75,73,81,66])
data.append([70,84,88,90,65,60])
data.append([60,40,55,58,47,49])
data.append([60,65,60,70,68,72])
data.append([95,98,85,87,93,95])
data.append([55,70,53,64,74,77])
data.append([50,53,57,63,58,40])
data.append([62,64,53,58,40,45])
# data.append([1,1])
# data.append([2,2])
# data.append([1,3])
# data.append([3,6])
# data.append([5,2])
# data.append([6,4])
# data.append([6,5])
# data.append([7,4])
# data.append([7,6])
# data.append([10,10])

# How many Cluster 
num_cluster = 3
# Treshold
treshold = 50/100

result = skcluster.AgglomerativeClustering(n_clusters=num_cluster,linkage='complete').fit_predict(data)

# *** CLUSTERING ***
# Make cluster from result
newCluster = []
for x in range(0,num_cluster):
    newCluster.append([])
for y in range(0,len(data)):
    # result 
    newCluster[result[y]].append(data[y])

# print(newCluster)
# *** FIND OUTLAYER ***
# For Every Cluster
index = 0
for d in newCluster:
    # print(" *** CLUSTER",index,"***")
    # Find MeanDistance of every data to data from that cluster
    distanceList = defaultdict(dict)
    mean = 0
    sumOfDistance = 0
    n = 0
    for i in range(0,len(d)):
        for ii in range(i+1,len(d)):
            dist = distance.euclidean(d[i],d[ii])
            distanceList[str(i)][str(ii)]=dist
            distanceList[str(ii)][str(i)]=dist
            sumOfDistance +=dist
            n+=1
    try:
        mean = sumOfDistance/n
        print(index,": radian =",mean*treshold)
    except:
        print("")
        # print(data.index(d[0]),"is outlayer because only one data")

    index+=1

    # Find which is bigger than MeanDistance
    for i in range(0,len(d)):
        tempDensity = 0
        for ii in range(0,len(d)):
            if(i!=ii):
                meanTreshold=mean*treshold
                if(distanceList[str(i)][str(ii)]>meanTreshold):
                    # Print them as outlayer
                    # print(i,",",ii,"is outlayer",distanceList[str(i)][str(ii)])
                    tempDensity+=1
                    # data.index()
                    # print("Index : ",data.index([50,53,57,63,58,40]))
        if(tempDensity==(len(d)-1)):
            print(data.index(d[i]),"is outlayer")
    
