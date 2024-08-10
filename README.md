# Dominant Color in Image
## Objective of the project :
There are three main parts to find the dominant colour .Firstly we read the image and get the RGB values of image 
using PIL library, this is the dataset for the k-mean clustering algorithm .
Then by using k-mean clustering algorithm ,we divide the data set into k sets, the question here arises is 
how many clusters is optimal, we can give algorithm any number of clusters .
Here comes the elbow method it finds the optimal number of clusters from the graph ,in this graph we plot 
number of clusters vs wcss (wcss is the sum of squares of the distances of each data point in all clusters to their 
respective centroids). It find the point where it look like a elbow joint (we are entering it manually ) this is the point 
of optimum clusters.
Then we calculate centroid of the clusters formed from k which we got from elbow plot, we take centroid 
of the cluster with most number of elements as final RGB for most dominating colour

