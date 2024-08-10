############################################### reading image #########################################################

image_path = input('enter the image path: ' )
from PIL import Image #import image module  from PIL library
im = Image.open(image_path) # reading image
im = im.resize((50, 50)) #resizing the image to decreaes the run time


r, g, b = list(im.getdata(0)), list(im.getdata(1)), list(im.getdata(2)) #getting r,g,b from image
x=[]
for i in range(len(r)):
    x.append([])
for i in range  (len(r)):  #getting rgb of a pixel into a single list
    x[i].append(r[i])
    x[i].append(g[i])
    x[i].append(b[i])
#print(len(x))


########################################################################################################################

############################################# k mean clusture code #####################################################

import random      #importing random and matplotlib libraries



def distan(x,y):    #this function calcuate the distace between two points
     l=(((x[0]-y[0])**2)+((x[1]-y[1])**2)+((x[2]-y[2])**2))**0.5  #using regular distance formula in coordinate system from mathematics
     return l


def listminimumindex(l):  #this function gives the index of the minimum element in list
     min = 0    #going from 0 to to last element for comparing
     for i in range (len(l)):
          if l[min]>l[i] :  #if ith element is less than min then replacing min with i value
               min = i
     return min     #returning the index

#print(listminimumindex(l))

def listmaximindex(l):  # this function gives the index of the maximum element in list
    maxm = 0  # going from 0 to to last element for comparing
    for i in range(len(l)):
        if l[maxm] < l[i]:  # if ith element is greater than max then replacing maximum with i value
            maxm = i
    return maxm

def distancelist(l,x): #this function finds the length of distance between a point and the centroid and return the centroid wich is least distance from the point
   output_list=[]      #l is list of points and x is a point,it finds which point of l is close to x
   for i in range(len(l)): #out_put is a list with all distance of pointsof l from x
     output_list.append(distan(l[i],x))
   return listminimumindex(output_list) #returning minimum value in the above list

#print(distancelist([[1,1],[1,2],[1,3],[1,4]],[1,2.5]))

def similar_check(l): #this function finds similar elements in list if it finds similar elements in list return 0
    for i in range (len(l)):
        for j in range(i+1,len(l)):
            if l[i]==l[j]: #this list compare all elements and find if there exist similar elements in list
                return 0  #returns 0 if any similar elements is found


def rand_dif_list(l,k): #this code select k different elements from l
    listrandom = random.sample(l, k)  #using random library to select k elements
    if similar_check(listrandom)==0: #if it found repititve elements it repeate the random selection process
        return rand_dif_list(l,k)
    else:        #if randomly selected list doesnt contain any similar elements
        return listrandom



def k_mean_cluster_r(l,k):#this function takes random point as centroid and assign all the points to the respective centre which is near
     nvariable=[] #if k=3 then nvariable is becoming [ [], [], [] ] ,elements of list of the list belong to the same clusture
     for i in range (k):
          nvariable.append([])
     len_of_list = len(l)
     listrandom = rand_dif_list(l,k) #taking a list with random unique points of rgb
     for i in range (len(l)):
          nvariable[distancelist(listrandom,l[i])].append(l[i]) #appending elements of l to respective clustures
     return [nvariable,listrandom]  #outputting the clustures and centroids of random list

#print(k_mean_cluster_r(X,8))


def centroidl(l): # finding the centroid of set of points
     cent=[0,0,0]  #this is simple mathematical calculation of centroid by adding all coordinates and dividing by number of coordinates
     for i in range (len(l)):
          cent[0] += l[i][0]
          cent[1] += l[i][1]
          cent[2] += l[i][2]
     cent[0]=cent[0]/len(l)
     cent[1]=cent[1]/len(l)
     cent[2]=cent[2]/len(l)
     return cent
#print(centroidl([[1,1],[1,2],[1,3],[1,4]]))


def k_mean_clusture_alpha(l,centre):#this function takes set of clustures and centres and give output as set of clusturewith respective centroid and is countinuation of k_mean_clusture_r
     sample_centre=[] #this list is to find the centroid of list l(l is  of type list in a list in a list
     for i in range(len(l)):
          sample_centre.append(centroidl(l[i]))

     if sample_centre == centre :#centroid of l matches with centreit gives back centre
          return centre
     else:
          x=[]
          for i in range(len(l)):  #if k=3 then x is becoming [ [], [], [] ] ,elements of list of the list belong to the same clusture
               x.append([])
          for i in range(len(l)):
               for j in range (len(l[i])): #re assigning points to respective clustre according to sample centre
                    x[distancelist(sample_centre, l[i][j])].append(l[i][j])
          return  k_mean_clusture_alpha(x,sample_centre)  #recursively finding the set where with centoid where above conditions satisfies
#print( k_mean_clusture_alpha((k_mean_cluster_r(x,2))[0],(k_mean_cluster_r(x,2))[1]))

def k_mean_clusture(l,k): #this function combines two function  k_mean_cluster_r(),k_mean_clusture_alpha() and returns the output
     return k_mean_clusture_alpha((k_mean_cluster_r(l,k))[0],(k_mean_cluster_r(l,k))[1])
#print(k_mean_clusture(x,1))

def elements_of_clusture(l,centre): #this is similar to k_mean_clusture_alpha()
    sample_centre=[] #this list is to find the centroid of list l(l is  of type list in a list in a list
    for i in range(len(l)):
          sample_centre.append(centroidl(l[i]))

    if sample_centre == centre :
          return l
    else:
          x=[]
          for i in range(len(l)):
               x.append([])
          for i in range(len(l)):
               for j in range (len(l[i])):
                    x[distancelist(sample_centre, l[i][j])].append(l[i][j])
          return  elements_of_clusture(x,sample_centre)






########################################################################################################################

################################################### elbow curve ########################################################



def wcss(l,k):  #In this function ,fFor each value of K, we are calculating WCSS ( Within-Cluster Sum of Square ).
                #WCSS is the sum of squared distance between each point and the centroid in a cluster
     centre = k_mean_clusture(l, k)  #we call back k mean clusture function to define centre

     out_put= 0                         #taking variable output as 0 initially
     for i in range (len(l)):           #taking range as length of list l , ie:
          x = []                        #defining variable x as empty list
          for j in range (len(centre)): #taking range as length of list obtained through k_mean_clusture which contains:
               x.append(distan(l[i],centre[j])) #x is appending all the distances from centre to point in l        
          out_put=out_put+(x[listminimumindex(x)])**2  # output is adding square of minimum value of distance
     return out_put         
     # returning output list containing values of wcss
#print(wcss([[1,1],[1,2],[1,3],[1,4]],1))
#print(wcss(x,8))


def elbow_curve(l):      #defing elbow curve, 
                                       
     x=[]                #we took empty list x ,
     for i in range(10): #and range which will basically be n int and k upto 10
          x.append([i+1,wcss(l,i+1)])   #and append n int and wcss values #eg: [1, wcss(rgb value list, k(which will be starting from 1))
     return x                           #returning final list x having two elements in each [i]list as [1,wcss] 
                                        #for which we will plot x-y graph next..


#print(elbow_curve(x))

list_elebow_curve = elbow_curve(x) # x is rgb values of given image,
                                   #this function call will give list output consisting [x,y] where x belongs to N from 1 to range 10
                                   #and y being wcss value
                                   
                         
x_axis=[]                                     #here two empty list : x_axis and
y_axis=[]                                     #y_axis are taken which will be appended to plot elbow graph
                                            
for i in range (len(list_elebow_curve)):      #with range being no. of elements in list_elebow_curve
    x_axis.append(list_elebow_curve[i][0])#we append k ( ie number of clusters) in x axis
for i in range (len(list_elebow_curve)):   #we append wcss ( ie total variation within sum of cluster) in y axis
    y_axis.append(list_elebow_curve[i][1])      #here we got two list for which graph will be plotted 




# here matplot lib is imported as pylot , it helps in plotting graph adn related functions
import matplotlib.pyplot as plt      


# plotting the points
plt.plot(x_axis,y_axis)

# naming the x axis
plt.xlabel('no.of clustures')
# naming the y axis
plt.ylabel('WCSS')

# giving a title to my graph
plt.title('elbow plot')

# function to show the plot
plt.show()

import matplotlib.pyplot as plt
def elements_highest_density(l): #defining function which will tell us most dominant colour in image by calculating density of given clusters
    x = []                       # x is empty list and l is list containing values of all rgb of given clusters as:
                                        #assuming k=3; ie number of clusters:
                                        # l=[[rgb value of all belong to this cluster c1],[rgb(c2)],[rgb(c3)]] just as an example

    for i in range(len(l)):      #here range will be no. of clusters ie k 
        x.append(len(l[i]))      #x is appending value which contains numbers of points(rgb)in given cluster

    return centroidl(l[listmaximindex(x)]) #whichever cluster have most elements will be most dense and therefore dominant colour of image


final_number_of_clustures=int(input('enter the optimum clusture from seeing elbow curve : ')) 

#this final rgb returns the centroid of clusture with highest density
final_rgb=[elements_highest_density(elements_of_clusture((k_mean_cluster_r(x,final_number_of_clustures))[0],(k_mean_cluster_r(x,final_number_of_clustures))[1]))]
for i in range(3):  #coverting final rgb into integers as rgb exist only in whol enumbers from 0 to 255
    final_rgb[0][i]=int( final_rgb[0][i])


print(final_rgb) #printing final rgb values
plt.imshow([final_rgb]) #showing image with final rgb values
plt.show() #showing plot of image
