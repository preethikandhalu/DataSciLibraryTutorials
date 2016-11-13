"""
REFERENCE
http://docs.scipy.org/doc/scipy/reference/tutorial/
"""
# -*- coding: utf-8 -*-
#As convention, all packages listed below should be imported
import numpy as np
import scipy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt

"""
Subpackage	Description
cluster	        Clustering algorithms
constants	Physical and mathematical constants
fftpack	        Fast Fourier Transform routines
integrate	Integration and ordinary differential equation solvers
interpolate	Interpolation and smoothing splines
io	        Input and Output
linalg	        Linear algebra
ndimage	        N-dimensional image processing
odr	        Orthogonal distance regression
optimize	Optimization and root-finding routines
signal	        Signal processing
sparse	        Sparse matrices and associated routines
spatial	        Spatial data structures and algorithms
special	        Special functions
stats	        Statistical distributions and functions
weave	        C/C++ integration

Scipy sub-packages need to be imported separetely, for example:
from scipy import linalg, optimize
"""

#######################BASIC FUNCTIONS

#######################INDEX FUNCTIONS
"""
There are some class instances that make special use of the slicing functionality
to provide efficient means for array construction. This part will discuss the
operation of np.mgrid , np.ogrid , np.r_ , and np.c_ for
quickly constructing arrays.
"""
a=np.concatenate([[3],[0]*5,np.arange(-1,1.002,2/9.0)])

#with the r_ (row concatenation) command, one can enter this as
b=np.r_[3,[0]*5,-1:1:10j]

#mgrid
"""
The real purpose of this function however is to produce N, N-d arrays which
provide coordinate arrays for an N-dimensional volume. 
however, this is not always needed just to evaluate some N-dimensional
function over a grid 
"""
c=np.mgrid[0:5,0:5]

"""
If this is the only purpose for generating a meshgrid, you should instead use the
function ogrid which generates an “open” grid using newaxis judiciously to create
N, N-d arrays where only one dimension in each array has length greater than 1.
This will save memory and create the same result if the only purpose for the
meshgrid is to generate sample points for evaluation of an N-d function.
"""

##########################POLYNOMIALS
#There are two (interchangeable) ways to deal with 1-d polynomials in SciPy.
#The first is to use the poly1d class from Numpy. This class accepts coefficients
#or polynomial roots to initialize a polynomial. The polynomial object can then be
#manipulated in algebraic expressions, integrated, differentiated, and evaluated.
#It even prints like a polynomial:

from numpy import poly1d
d=poly1d([3,4,5])
print "d"
print d
print "integral of d"
print d.integ()
print "derivative of d"
print d.deriv()
e=d([4,5])  #evaluates d when x==4 and x=5


#########################VECTORIZING FUNCTIONS
"""
One of the features that NumPy provides is a class vectorize to convert an
ordinary Python function which accepts scalars and returns scalars into a
“vectorized-function” with the same broadcasting rules as other Numpy functions
(i.e. the Universal functions, or ufuncs). For example, 
"""
def addsubtract(a,b):
    if a>b:
        return a-b
    else:
        return a+b

vec_addsubtract=np.vectorize(addsubtract)
ans=vec_addsubtract([0,3,6,9],[1,3,5,7])

#############################GENERAL
#to get just the real/imag part of a complex number
f=32904832905
g=np.real(f)
h=np.imag(f)
#can also use np.real_if_close which transforms a complex-valued number with tiny
#imaginary part into a real number

#to check whether a number is scalar. Bool function
i=324
j=np.array([324,234])
k=np.isscalar(i)
l=np.isscalar(j)

#ensuring that objects are a certain Numpy type occurs often enough that it
#has been given a convenient interface in SciPy through the use of the
#np.cast dictionary.
m=np.cast['f'](np.pi)

#another useful function is the SELECT function.
#DONT UNDERSTAND AT ALL!!!!!
"""
select(condlist,choicelist,default=0). select is a vectorized form of the multiple
if-statement. It allows rapid construction of a function which returns an array
of results based on a list of conditions. Each element of the return array is taken
from the array in a choicelist corresponding to the first condition in condlist that
is true. For example
"""
n=np.r_[-2:3]
o=np.select([n>3,n>=0],[0,n+2])
