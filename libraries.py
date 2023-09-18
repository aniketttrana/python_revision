# Numpy stands for Numerical Python and it is the core library for numeric and scientific computing
    
# first install numpy
# pip install numpy
# It consist of multi-dimensional array objects and a collection of routines for processing those arrays

##############Single Dimension 
import numpy as np
n1=np.array([1,2,3,4])
print(n1)
print(type(n1))
############## multidimensional
import numpy as np
n2=np.array([[1,2,3,4],[5,6,7,8]])
# list of list
print(n2)
print(type(n1))

############# initializing Numpy array with zeros #####
n3=np.zeros((1,2))
# 1 row and 3 coloumn
print(n3)

n3=np.zeros((5,5))
print(n3)

# Initializing NumPy array with same number

n4=np.full((2,2),10)
# 2*2 ka jisme value 10 ho
print(n4)

# to get all the elements in the given range
n5=np.arange(10,20)
# 20 not included
print(n5)

# To make some addition in it
n6=np.arange(10,50,5)
# it will print 10 se 50 se peeche tak with 5  difference
print(n6)


# ####
n7=np.random.randint(1,100,5)
# upto 5 values
print(n7)

############TO change row and coloumn of array 
n8=np.array([[1,2,3,4],[4,3,2,1]])
print(n8)
n8.shape=(4,2)
print(n8)

########### To Concatenate the arrays
n9=np.array([10,20,30])
n10=np.array([40,50,60])
# vertically
np.vstack((n9,n10))
np.hstack((n9,n10))
np.column_stack((n9,n10))

# ######## Intersection of arrays
n11=np.array([10,20,30,40,50])
n12=np.array([50,60,70,80,90,100])
# Intersection(common elements)
res=np.intersect1d(n11,n12)
print(res)
# To find unique element in n11
res1=np.setdiff1d(n11,n12)
print(res1)
# To find unique element in n12
res2=np.setdiff1d(n12,n11)
print(res2)

################ Adition of two arrays

n13=np.array([10,20])
n14=np.array([30,40])
summ=np.sum([n13,n14])
print(summ)

# to add it by coloumn
summ=np.sum([n13,n14],axis=0)
print(summ)
# to add it by row wise
summ=np.sum([n13,n14],axis=1)
print(summ)

######################## Basic Addition in arrays
n15=np.array([10,20,30])
n15=n15+1
# n15=n15-1
# n15=n15-1
# n15=n15*2
# n15=n15/2
print(n15)

m=np.mean(n15)
print(m)
med=np.median(n15)
print(med)
sd=np.std(n15)
print(sd)

#################  save & load
n16=np.array([1,2,3,4])
np.save('my_numpy',n16)
print(n16)

n17=np.load('my_numpy.npy')
print(n17)
