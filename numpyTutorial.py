"""
REFERENCE
http://scipy.github.io/old-wiki/pages/Tentative_NumPy_Tutorial.html

Some methods/attributes -
- array()

- arange()
- linspace()
- random.random([])

- zeros()
- ones()
- empty()

- reshape()
- resize()
- shape
- size
- ndim
- dtype
- itemsize

# for below four methods, can use axes as argument as well
- sum()
- cumsum()  
- min()
- max()

- dot()

- ravel()
- flat

- vstack()
- hstack()

- hsplit()
- vsplit()

- view()
- copy()
"""

from numpy import *

######################################TO CREATE ARRAY OF NUMBERS
#to create sequence of numbers, numpy has a fxn analagous to range,
#returns arrays instead of lists
#returns 10-30 with step5
r= arange(10,30,5)

#can use floats as well
r2=arange(0,2,0.3)

#another super useful function
#returns an array with 9 numbers beween 0 and 2
lin=linspace(0,2,9)

#random
ran=random.random([2,3])

#Often, the elements of an array are originally unknown, but its size is known.
#Hence, NumPy offers several functions to create arrays with initial
#placeholder content. These minimize the necessity of growing arrays,
#an expensive operation.
z=zeros([2,4])

o=ones([2,3,4])

#random values from memory
em = empty([2,3])

#####################################BASIC ARRAY FUNCTIONALITY
#numbers from 0-14 shaped into a 3x5 matrix
a=arange(15).reshape(3,5)

#nxm
shape=a.shape

#2D array
dim=a.ndim

#type of data in array
ty=a.dtype.name

#no. of items in matrix
count=a.size

#no. of bytes per element
byte=a.itemsize


##frequest mistake
"""
b=array(2,42,1) #WRONG
"""
b=array([2,42,1])   #RIGHT

#to create 2D, 3D arrays
c=array([[1,2,3], [4,5,6], [7,8,9]])

#dtype of array can also be explicityl specified at creation
d = array([[1,2],[3,4]], dtype=complex)

########################################PRINTING ARRAYS
#When you print an array, NumPy displays it in a similar way to nested lists,
#but with the following layout:
# * the last axis is printed from left to right,
# * the second-to-last is printed from top to bottom,
# * the rest are also printed from top to bottom, with each slice separated
#   from the next by an empty line.

e = arange(6)   #1D array

f = arange(12).reshape(4,3)     #2D array

g = arange(24).reshape(2,3,4)   #3D array


#Note: if array is too large, numpy automatically skips central part of array
#and only prints the corners
#ex: print arange(10000)
#to disable this behavior: set_printoptions(threshold='nan')

#######################################BASIC OPERATIONS
h=array([20,30,40,50])
i=arange(4)

sum_=i.sum()
min_=i.min()
max_=i.max()

j=h-i

isq=i**2

k=10*sin(h)

l=h<35

A=array([[1,1],[0,1]])
B=array([[2,0],[3,4]])

#elementwise product
el=A*B

#matrix product
ma=dot(A,B)


C=arange(12).reshape(3,4)
sumi = C.sum(axis=0)    #sum of each column....0 refers to 4
mini = C.min(axis=1)    #min of each row...1 refers to 3
cumsum = C.cumsum(axis=1)   #cumulative sum along each row

#####################DIDNT DO UNIVERSAL FUNCTIONS

#####################INDEXING, SLICING AND ITERATING
#onedimensaional
m=arange(10)**3
m2=m[2]
m25=m[2:5]
m[:6:2]=-1000
m=m[::-1]

#multidimensional
n=arange(25).reshape(5,5)
n23=n[2,3]          #3rd row, 4th column
n051=n[0:5, 1]      #each row in the second col
n1=n[:,1]           #equiv. to prev example
n13=n[1:3,:]

#dots
#notice that for every axis, you need a :
#ex: n[,1] results in an error..you need n[:,1]
#easy to have : when dim is small
#when you have a lot of dim, alternative is '...'
#For example
#x[1,2,...] is equivalent to x[1,2,:,:,:],
#x[...,3] to x[:,:,:,:,3] and
#x[4,...,5,:] to x[4,:,:,5,:]

#iterating
o=arange(25).reshape(5,5)
def printo():
    for row in o:
        print row

def printi():
    for i in o.flat:
        print i
###########################SHAPE MANIPULATION
p=arange(12).reshape(3,4)
p=p.ravel()     #to flatten
p.shape=(6,2)   #resize method same does same thing as shape... p.resize([6,2])
#reshape function returns argument with modified shape, resize modifies the array itself
#instead of ravelling, could have also used reshape
#if dimension is given as -1, other dimensions are automatically calculated
#only one dimension can be -1

########################STACKING TOGETHER DIFFERENT ARRAYS
D=floor(10*random.random((2,2)))
E=floor(10*random.random((2,2)))
vstack=vstack([D,E])        #vertical stack
hstack=hstack([D,E])        #horizontal stack

#The function column_stack stacks 1D arrays as columns into a 2D array.
#It is equivalent to vstack only for 1D arrays

#The function row_stack, on the other hand, stacks 1D arrays as
#rows into a 2D array.

#splitting one array into several smaller ones
q=floor(10*random.random((2,12)))
qsplit = hsplit(q,3)   # Split q into 3
hsplit34=hsplit(q,(3,5))   # Split q so that col 0-2 are 1 array, col3-4 are one array and the rest is another array
#can use vsplit as well

##############################COPIES AND VIEWS
#NO COPY AT ALL
#Simple assignments make no copy of array objects or of their data.
q=arange(12)
r=q     #no new objest is created
r.shape=(3,4)   #changes the shape of q

#VIEW OR SHALLOW COPY
#Different array objects can share the same
#data. The view method creates a new array object that looks at the same data.
s=arange(12)
t=s.view()
t.shape=(3,4)       #s shape doesnt change
t[4]=234234         #s data also changes

#DEEP COPY
#The copy method makes a complete copy of the array and its data.
u=arange(12)
v=u.copy()      #v doesnt share anything this u

##########STOPPED AT LESS BASIC
