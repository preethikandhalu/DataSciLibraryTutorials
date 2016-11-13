"""
REFERENCE
http://pandas.pydata.org/pandas-docs/stable/10min.html
http://pandas.pydata.org/pandas-docs/stable/dsintro.html#dsintro
^ DSINTRO IS VERY IMPORTANT LINK
http://www.gregreda.com/2013/10/26/intro-to-pandas-data-structures/
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab

###########################################################################
###########################################################################
##FIRST AND SECOND REFERNECE
###########################################################################
###########################################################################
"""
 
SERIES
Series is a one-dimensional labeled array capable of holding any data type
(integers, strings, floating point numbers, Python objects, etc.). The axis
labels are collectively referred to as the index. 

DATA FRAMES
DataFrame is a 2-dimensional labeled data structure with columns of potentially
different types. You can think of it like a spreadsheet or SQL table
Like Series, DataFrame accepts many different kinds of input:
- Dict of 1D ndarrays, lists, dicts, or Series
- 2-D numpy.ndarray
- Structured or record ndarray
- A Series
- Another DataFrame
"""

##################################OBJECT CREATION
#SERIES
r=pd.Series(range(9))
s = pd.Series([1,3,5,np.nan,6,8], index=['a','b','c','d','e','f'])

#DATA FRAMES
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

#creating a data frame from a dict
df2 = pd.DataFrame({ 'A' : 1.,'B' : pd.Timestamp('20130102'),'C' : pd.Series(1,index=list(range(4)),dtype='float32'), 'D' : np.array([3] * 4,dtype='int32'),'E' : pd.Categorical(["test","train","test","train"]), 'F' : 'foo' })

#view the head/tail of the frame
head = df.head()
head2 = df.head(3)
tail = df.tail(2)

#get index, columns, values separately
ind = df.index
col = df.columns
val = df.values

#quick statistic summary of the data
stat = df.describe()

#transposing
tr = df.T

#sort by axis
#DONT UNDERSTAND!
so = df.sort_index(axis=1, ascending=False)

#sort by values
va = df.sort_values(by='B')

#####################################SELECTION
#SELECTION BY LABEL
#to select a single column
A=df['A']

#slicing rows
r=df[0:3]
d=df['20130102':'20130103']

#selection by label
da= df.loc[dates[0],:]
co = df.loc[:,['A','B']]
bo = df.loc['20130102':'20130104',['A','B']]
#for getting a scalar value
v = df.loc[dates[0],'A']
v2 = df.at[dates[0],'A']    #for faster access

#SELECTION BY POSITION
row4=df.iloc[3]
a=df.iloc[3:5,0:2]
b=df.iloc[[1,2,4],[0,2]]
c=df.iloc[1:3,:]
d=df.iloc[:,1:3]
#for getting a scalar value
v3= df.iloc[1,1]
v4= df.iat[1,1]             #for faster access

#################################BOOLEAN INDEXING
b1=df[df.A > 0]
b2=df[df > 0]
#using isin() method for filtering
df2=df.copy()
df2['E']=['one', 'one', 'two', 'three','four', 'three']
sorcery=df2[df2['E'].isin(['two','four'])]

#################################SETTING
s1 = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130102', periods=6))
df['F'] = s1            #setting a column
df.at[dates[0],'A'] = 0         #setting by label
df.iat[0,1] = 0                 #setting by position
df.loc[:,'D'] = np.array([5] * len(df))     #setting a column

df3=df.copy()
df3[df3>0] = -df3

#################################MISSING DATA
"""
pandas primarily uses the value np.nan to represent missing data.
It is by default not included in computations
"""
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
df1.loc[dates[0]:dates[1], 'E']=1
df1.dropna(how='any')   #drop rows having missing data
df1.fillna(value=5)     #filling missing data
pd.isnull(df1)          #to see where data is null

###################################OPERATIONS
#STATS
#Operations in general exclude missing data
mean = df.mean()    #mean column wise
mean2 = df.mean(1)  #mean row wise

#APPLY
#Applying functions to a data
cum = df.apply(np.cumsum)
rang1 = df.apply(lambda x: x.max() - x.min())

#HISTOGRAMMIN'
s2 = pd.Series(np.random.randint(0, 7, size=10))
cout=s2.value_counts()

#STRING METHODS
s3=pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
slow= s3.str.lower()

###################################MERGE
#CONCAT
"""
pandas provides various facilities for easily combining together Series,
DataFrame, and Panel objects with various kinds of set logic for the indexes
and relational algebra functionality in the case of join /
merge-type operations.
"""
df4 = pd.DataFrame(np.random.randn(10, 4))
pieces = [df4[:3], df4[3:7], df4[7:]]
con = pd.concat(pieces)

#JOIN
#SQL style merges
left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
join= pd.merge(left, right, on='key')

#APPEND
#append rows to a dataframe
df5 = pd.DataFrame(np.random.randn(8, 4), columns=['A','B','C','D'])
s=df5.iloc[3]
df5=df5.append(s, ignore_index=True)
#must be careful. thought df5 would auto. append to df5...but append() returns
#df5 with the appended thing
#ie. just df5.append() isn't enough. gotta do df5=df5.append()

#GROUPING
df6 = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],'B' : ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'], 'C' : np.random.randn(8), 'D' : np.random.randn(8)})
group=df6.groupby('A').sum()
group2=df6.groupby(['A','B']).sum()

"""
DIDN'T DO RESHAPING
DIDN'T DO TIME SERIES
DIDN'T DO CATEGORICALS
DIDN'T DO PLOTTING
"""

##################################GETTING DATA IN/OUT
"""
CSV
writing to a csv file
df.to_csv('foo.csv')

reading from a csv file
pd.read_csv('foo.csv')

HDF5
writing to a HDF5 store
df.to_hdf('foo.h5','df')

reading from a HDF5 store
pd.read_hdf('foo.h5','df')

EXCEL
writing to an excel file
df.to_excel('foo.xlsx', sheet_name='Sheet1')

reading from an excel file
pd.read_excel('foo.xlsx', 'Sheet1', index_col=None, na_values=['NA'])
"""

###########################################################################
###########################################################################
#THIRD REFERENCE
###########################################################################
###########################################################################

######################################
#PART1. INTRO TO PANDAS DATA STRUCTURE
######################################
"""
WHAT IS PANDAS?
pandas is an open source Python library for data analysis. Python has always
been great for prepping and munging data, but it's never been great for
analysis - you'd usually end up using R or loading it into a database and
using SQL (or worse, Excel). pandas makes Python great for analysis.
"""

##########################################SERIES
"""
A Series is a one-dimensional object similar to an array, list, or column in
a table. It will assign a labeled index to each item in the Series. By default,
each item will receive an index label from 0 to N, where N is the length of the
Series minus one.

Basically a dictionary
"""
f=pd.Series([7, 'Heidelberg', 3.14, -1.3434, 'Happy panda-ing!'])

#can also specify index
g=pd.Series([7, 'Heidelberg', 3.14, -1.3434, 'Happy panda-ing!'], index=['A', 'C', 'E', 'G', 'P'])

#can also convert dict to Series
dicti = {'Chicago': 1000, 'New York': 1300, 'Portland': 900, 'San Francisco': 1100, 'Austin': 450, 'Boston': None}
cities=pd.Series(dicti)

#can use series as a dict, can also specify multiple parameters
ex=cities[['Chicago', 'Portland', 'San Francisco']]

#can also use boolean indexing for selection
ex2=cities[cities<1000] #cities<1000 returns a series of T/F values

#can also change values in the series
cities['Chicago']=1400

#change using boolean logic
cities[cities<1000]=750

#can also do mathematical operations
cities2=cities/3
square=np.square(cities)

#to check whether an item is in series
chk1= "Seattle" in cities
chk2= "San Francisco" in cities

#can add two series
add=cities[['Chicago', 'New York', 'Portland']] + cities[['Austin', 'New York']]

#null checking can be performed with isnull() and notnull() functions
ex3=cities.isnull()

##########################################DATA FRAME
"""
A DataFrame is a tablular data structure comprised of rows and columns, akin to
a spreadsheet, database table, or R's data.frame object. You can also think of
a DataFrame as a group of Series objects that share an index (the row names).
"""
#Reading data
data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012], 'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions', 'Lions', 'Lions'], 'wins': [11, 8, 10, 15, 11, 6, 10, 4], 'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
football = pd.DataFrame(data, columns=['year','team','wins','losses'])

#ref has more info regarding reading from CSV, Excel, Database, Clipboard, URL

################################
#PART2. WORKING WITH DATA FRAMES
################################

#Using MovieLens dataset
#pass in column names for each CSV

"""
u_cols=['user_id', 'age', 'sex', 'occupation', 'zip-code']
users = pd.read_csv('ml-100k/u.user', sep= '|', names=u_cols, encoding='latin-1')
"""
u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
u_path =r"/home/preethikandhalu/Desktop/Coding/Misc/DataSciTutorials/ml-100k/u.user"
users = pd.read_csv(u_path, sep='|', names=u_cols, encoding='latin-1')

r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
r_path =r"/home/preethikandhalu/Desktop/Coding/Misc/DataSciTutorials/ml-100k/u.data"
ratings = pd.read_csv(r_path, sep='\t', names=r_cols, encoding='latin-1')

# the movies file contains columns indicating the movie's genres
# let's only load the first five columns of the file with usecols
m_cols = ['movie_id', 'title', 'release_date', 'video_release_date', 'imdb_url']
m_path=r"/home/preethikandhalu/Desktop/Coding/Misc/DataSciTutorials/ml-100k/u.item"
movies = pd.read_csv(m_path, sep='|', names=m_cols, usecols=range(5), encoding='latin-1')

