#### 1. Import the numpy package under the name `np` (★☆☆)
import numpy as np

#### 2. Print the numpy version and the configuration (★☆☆)
# print(np.__version__)
# np.show_config()

#### 3. Create a null vector of size 10 (★☆☆)
Z = np.zeros(10)
# print(Z)

#### 4. How to find the memory size of any array (★☆☆)
Z = np.zeros((10,10))
# print("%d bytes" % (Z.size * Z.itemsize))

#### 5. How to get the documentation of the numpy add function from the command line? (★☆☆)
# %run `python -c "import numpy; numpy.info(numpy.add)"`

#### 6. Create a null vector of size 10 but the fifth value which is 1 (★☆☆)
Z = np.zeros(10)
Z[4] = 1
# print(Z)

#### 7. Create a vector with values ranging from 10 to 49 (★☆☆)
Z = np.arange(10,50)
# print(Z)

#### 8. Reverse a vector (first element becomes last) (★☆☆)
Z = np.arange(50)
Z = Z[::-1]
# print(Z)

#### 9. Create a 3x3 matrix with values ranging from 0 to 8 (★☆☆)
Z = np.arange(9).reshape(3, 3)
# print(Z)

#### 10. Find indices of non-zero elements from [1,2,0,0,4,0] (★☆☆)
nz = np.nonzero([1,2,0,0,4,0])
# print(nz)

#### 11. Create a 3x3 identity matrix (★☆☆)
Z = np.eye(3)
# print(Z)

#### 12. Create a 3x3x3 array with random values (★☆☆)
Z = np.random.random((3,3,3))
# print(Z)

#### 13. Create a 10x10 array with random values and find the minimum and maximum values (★☆☆)
Z = np.random.random((10,10))
Zmin, Zmax = Z.min(), Z.max()
# print(Z, Zmin, Zmax)

#### 14. Create a random vector of size 30 and find the mean value (★☆☆)
Z = np.random.random(30)
m = Z.mean()
# print(m)

#### 15. Create a 2d array with 1 on the border and 0 inside (★☆☆)
Z = np.ones((10,10))
Z[1:-1,1:-1] = 0
# print(Z)

#### 16. How to add a border (filled with 0's) around an existing array? (★☆☆)
Z = np.ones((5,5))
Z = np.pad(Z, pad_width=1, mode='constant', constant_values=0)
# print(Z)

# Using fancy indexing
Z[:, [0, -1]] = 0
Z[[0, -1], :] = 0
# print(Z)

#### 17. What is the result of the following expression? (★☆☆0 * np.nan
np.nan == np.nan
np.inf > np.nan
np.nan - np.nan
np.nan in set([np.nan])
0.3 == 3 * 0.1

# print(0 * np.nan)
# print(np.nan == np.nan)
# print(np.inf > np.nan)
# print(np.nan - np.nan)
# print(np.nan in set([np.nan]))
# print(0.3 == 3 * 0.1)

#### 18. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal (★☆☆)
Z = np.diag(1+np.arange(4),k=-1)
# print(Z)

#### 19. Create a 8x8 matrix and fill it with a checkerboard pattern (★☆☆)
Z = np.zeros((8,8),dtype=int)
Z[1::2,::2] = 1
Z[::2,1::2] = 1
# print(Z)

#### 20. Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element? (★☆☆)
# print(np.unravel_index(99,(6,7,8)))

#### 21. Create a checkerboard 8x8 matrix using the tile function (★☆☆)
Z = np.tile( np.array([[0,1],[1,0]]), (4,4))
# print(Z)

#### 22. Normalize a 5x5 random matrix (★☆☆)
Z = np.random.random((5,5))
Z = (Z - np.mean (Z)) / (np.std (Z))
# print(Z)

#### 23. Create a custom dtype that describes a color as four unsigned bytes (RGBA) (★☆☆)
color = np.dtype([("r", np.ubyte),
                    ("g", np.ubyte),
                    ("b", np.ubyte),
                    ("a", np.ubyte)])
# print(color)

#### 24. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product) (★☆☆)
Z = np.dot(np.ones((5,3)), np.ones((3,2)))
# print(Z)

# Alternative solution, in Python 3.5 and above
Z = np.ones((5,3)) @ np.ones((3,2))
# print(Z)

#### 25. Given a 1D array, negate all elements which are between 3 and 8, in place. (★☆☆)

Z = np.arange(11)
Z[(3 < Z) & (Z < 8)] *= -1
# print(Z)

#### 26. What is the output of the following script? (★☆

# print(sum(range(5),-1))
from numpy import *
# print(sum(range(5),-1))

# print(sum(range(5),-1))
from numpy import *
# print(sum(range(5),-1))

#### 27. Consider an integer vector Z, which of these expressions are legal? (★☆
# Z**Z
# 2 << Z >> 2
# Z <- Z
# 1j*Z
# Z/1/1
# Z<Z>Z

# Z**Z
# 2 << Z >> 2
# Z <- Z
# 1j*Z
# Z/1/1
# Z<Z>Z

#### 28. What are the result of the following expressions? (★☆
# np.array(0) / np.array(0)
# np.array(0) // np.array(0)
# np.array([np.nan]).astype(int).astype(float)

# print(np.array(0) / np.array(0))
# print(np.array(0) // np.array(0))
# print(np.array([np.nan]).astype(int).astype(float))

#### 29. How to round away from zero a float array ? (★☆☆)
Z = np.random.uniform(-10,+10,10)
# print(np.copysign(np.ceil(np.abs(Z)), Z))

# More readable but less efficient
# print(np.where(Z>0, np.ceil(Z), np.floor(Z)))

#### 30. How to find common values between two arrays? (★☆☆)
Z1 = np.random.randint(0,10,10)
Z2 = np.random.randint(0,10,10)
# print(np.intersect1d(Z1,Z2))

#### 31. How to ignore all numpy warnings (not recommended)? (★☆☆)

# Suicide mode on
defaults = np.seterr(all="ignore")
Z = np.ones(1) / 0

# Back to sanity
_ = np.seterr(**defaults)

# Equivalently with a context manager
with np.errstate(all="ignore"):
    np.arange(3) / 0

#### 32. Is the following expressions true? (★☆☆)
# np.sqrt(-1) == np.emath.sqrt(-1)

#### 33. How to get the dates of yesterday, today and tomorrow? (★☆☆)

yesterday = np.datetime64('today') - np.timedelta64(1)
today     = np.datetime64('today')
tomorrow  = np.datetime64('today') + np.timedelta64(1)

#### 34. How to get all the dates corresponding to the month of July 2016? (★★☆)

Z = np.arange('2016-07', '2016-08', dtype='datetime64[D]')
# print(Z)

#### 35. How to compute ((A+B)*(-A/2)) in place (without copy)? (★★☆)

A = np.ones(3)*1
B = np.ones(3)*2
np.add(A,B,out=B)
np.divide(A,2,out=A)
np.negative(A,out=A)
np.multiply(A,B,out=A)

#### 36. Extract the integer part of a random array of positive numbers using 4 different methods (★★☆)

Z = np.random.uniform(0,10,10)

# print(Z - Z%1)
# print(Z // 1)
# print(np.floor(Z))
# print(Z.astype(int))
# print(np.trunc(Z))

#### 37. Create a 5x5 matrix with row values ranging from 0 to 4 (★★☆)

Z = np.zeros((5,5))
Z += np.arange(5)
# print(Z)

# without broadcasting
Z = np.tile(np.arange(0, 5), (5,1))
# print(Z)

#### 38. Consider a generator function that generates 10 integers and use it to build an array (★☆☆)

def generate():
    for x in range(10):
        yield x
Z = np.fromiter(generate(),dtype=float,count=-1)
# print(Z)

#### 39. Create a vector of size 10 with values ranging from 0 to 1, both excluded (★★☆)

Z = np.linspace(0,1,11,endpoint=False)[1:]
# print(Z)

#### 40. Create a random vector of size 10 and sort it (★★☆)

Z = np.random.random(10)
Z.sort()
# print(Z)

#### 41. How to sum a small array faster than np.sum? (★★☆)

Z = np.arange(10)
np.add.reduce(Z)

#### 42. Consider two random array A and B, check if they are equal (★★☆)

A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)

# Assuming identical shape of the arrays and a tolerance for the comparison of values
equal = np.allclose(A,B)
# print(equal)

# Checking both the shape and the element values, no tolerance (values have to be exactly equal)
equal = np.array_equal(A,B)
print(equal)

#### 43. Make an array immutable (read-only) (★★☆)

Z = np.zeros(10)
Z.flags.writeable = False
# Z[0] = 1

#### 44. Consider a random 10x2 matrix representing cartesian coordinates, convert them to polar coordinates (★★☆)

Z = np.random.random((10,2))
X,Y = Z[:,0], Z[:,1]
R = np.sqrt(X**2+Y**2)
T = np.arctan2(Y,X)
# print(R)
# print(T)

#### 45. Create random vector of size 10 and replace the maximum value by 0 (★★☆)

Z = np.random.random(10)
Z[Z.argmax()] = 0
# print(Z)

#### 46. Create a structured array with `x` and `y` coordinates covering the [0,1]x[0,1] area (★★☆)

Z = np.zeros((5,5), [('x',float),('y',float)])
Z['x'], Z['y'] = np.meshgrid(np.linspace(0,1,5),
np.linspace(0,1,5))
# print(Z)

#### 47. Given two arrays, X and Y, construct the Cauchy matrix C (Cij =1/(xi - yj)) (★★☆)

X = np.arange(8)
Y = X + 0.5
C = 1.0 / np.subtract.outer(X, Y)
# print(np.linalg.det(C))

#### 48. Print the minimum and maximum representable value for each numpy scalar type (★★☆)

for dtype in [np.int8, np.int32, np.int64]:
    print(np.iinfo(dtype).min)
    print(np.iinfo(dtype).max)
for dtype in [np.float32, np.float64]:
    print(np.finfo(dtype).min)
    print(np.finfo(dtype).max)
    print(np.finfo(dtype).eps)

#### 49. How to print all the values of an array? (★★☆)

np.set_printoptions(threshold=float("inf"))
Z = np.zeros((40,40))
# print(Z)

#### 50. How to find the closest value (to a given scalar) in a vector? (★★☆)

Z = np.arange(100)
v = np.random.uniform(0,100)
index = (np.abs(Z-v)).argmin()
# print(Z[index])

#### 51. Create a structured array representing a position (x,y) and a color (r,g,b) (★★☆)
Z = np.zeros(10, [ ('position', [ ('x', float, 1),
                                ('y', float, 1)]),
                                ('color',    [ ('r', float, 1),
                                ('g', float, 1),
                                ('b', float, 1)])])
# print(Z)

#### 52. Consider a random vector with shape (100,2) representing coordinates, find point by point distances (★★☆)
Z = np.random.random((10,2))
X,Y = np.atleast_2d(Z[:,0], Z[:,1])
D = np.sqrt( (X-X.T)**2 + (Y-Y.T)**2)
print(D)


#### 53. How to convert a float (32 bits) array into an integer (32 bits) in place?

# & unutbu (https://stackoverflow.com/a/4396247/5989906)
Z = (np.random.rand(10)*100).astype(np.float32)
Y = Z.view(np.int32)
Y[:] = Z
print(Y)

#### 54. How to read the following file? (★★☆)

# 1, 2, 3, 4, 5
# 6,  ,  , 7, 8
# ,  , 9,10,11


from io import StringIO

# Fake file
s = StringIO('''1, 2, 3, 4, 5

                6,  ,  , 7, 8

                ,  , 9,10,11
''')
Z = np.genfromtxt(s, delimiter=",", dtype=np.int)
print(Z)

#### 55. What is the equivalent of enumerate for numpy arrays? (★★☆)

Z = np.arange(9).reshape(3,3)
for index, value in np.ndenumerate(Z):
    print(index, value)
for index in np.ndindex(Z.shape):
    print(index, Z[index])

#### 56. Generate a generic 2D Gaussian-like array (★★☆)

X, Y = np.meshgrid(np.linspace(-1,1,10), np.linspace(-1,1,10))
D = np.sqrt(X*X+Y*Y)
sigma, mu = 1.0, 0.0
G = np.exp(-( (D-mu)**2 / ( 2.0 * sigma**2 ) ) )
print(G)

#### 57. How to randomly place p elements in a 2D array? (★★☆)

n = 10
p = 3
Z = np.zeros((n,n))
np.put(Z, np.random.choice(range(n*n), p, replace=False),1)
print(Z)

#### 58. Subtract the mean of each row of a matrix (★★☆)

X = np.random.rand(5, 10)

# Recent versions of numpy
Y = X - X.mean(axis=1, keepdims=True)

# Older versions of numpy
Y = X - X.mean(axis=1).reshape(-1, 1)

print(Y)

#### 59. How to sort an array by the nth column? (★★☆)

Z = np.random.randint(0,10,(3,3))
print(Z)
print(Z[Z[:,1].argsort()])

#### 60. How to tell if a given 2D array has null columns? (★★☆)

# null : 0 
Z = np.random.randint(0,3,(3,10))
print((~Z.any(axis=0)).any())

# null : np.nan
Z=np.array([
    [0,1,np.nan],
    [1,2,np.nan],
    [4,5,np.nan]
])
print(np.isnan(Z).all(axis=0))

#### 61. Find the nearest value from a given value in an array (★★☆)


Z = np.random.uniform(0,1,10)
z = 0.5
m = Z.flat[np.abs(Z - z).argmin()]
print(m)

#### 62. Considering two arrays with shape (1,3) and (3,1), how to compute their sum using an iterator? (★★☆)


A = np.arange(3).reshape(3,1)
B = np.arange(3).reshape(1,3)
it = np.nditer([A,B,None])
for x,y,z in it: z[...] = x + y
print(it.operands[2])

#### 63. Create an array class that has a name attribute (★★☆)

class NamedArray(np.ndarray):
    def __new__(cls, array, name="no name"):
        obj = np.asarray(array).view(cls)
        obj.name = name
        return obj
    def __array_finalize__(self, obj):
        if obj is None: return
        self.name = getattr(obj, 'name', "no name")

Z = NamedArray(np.arange(10), "range_10")
print (Z.name)

#### 64. Consider a given vector, how to add 1 to each element indexed by a second vector (be careful with repeated indices)? (★★★)

Z = np.ones(10)
I = np.random.randint(0,len(Z),20)
Z += np.bincount(I, minlength=len(Z))
print(Z)

# Another solution
np.add.at(Z, I, 1)
print(Z)

#### 65. How to accumulate elements of a vector (X) to an array (F) based on an index list (I)? (★★★)

X = [1,2,3,4,5,6]
I = [1,3,9,3,4,1]
F = np.bincount(I,X)
print(F)

#### 66. Considering a (w,h,3) image of (dtype=ubyte), compute the number of unique colors (★★☆)

w, h = 256, 256
I = np.random.randint(0, 4, (h, w, 3)).astype(np.ubyte)
colors = np.unique(I.reshape(-1, 3), axis=0)
n = len(colors)
print(n)

# Faster version
# https://stackoverflow.com/a/59671950/2836621

w, h = 256, 256
I = np.random.randint(0,4,(h,w,3), dtype=np.uint8)

# View each pixel as a single 24-bit integer, rather than three 8-bit bytes
I24 = np.dot(I.astype(np.uint32),[1,256,65536])

# Count unique colours
n = len(np.unique(I24))
print(n)

#### 67. Considering a four dimensions array, how to get sum over the last two axis at once? (★★★)


A = np.random.randint(0,10,(3,4,3,4))
# solution by passing a tuple of axes (introduced in numpy 1.7.0)
sum = A.sum(axis=(-2,-1))
print(sum)
# solution by flattening the last two dimensions into one
# (useful for functions that don't accept tuples for axis argument)
sum = A.reshape(A.shape[:-2] + (-1,)).sum(axis=-1)
print(sum)

#### 68. Considering a one-dimensional vector D, how to compute means of subsets of D using a vector S of same size describing subset  indices? (★★★)

D = np.random.uniform(0,1,100)
S = np.random.randint(0,10,100)
D_sums = np.bincount(S, weights=D)
D_counts = np.bincount(S)
D_means = D_sums / D_counts
print(D_means)

# Pandas solution as a reference due to more intuitive code
# print(pd.Series(D).groupby(S).mean())

#### 69. How to get the diagonal of a dot product? (★★★)

A = np.random.uniform(0,1,(5,5))
B = np.random.uniform(0,1,(5,5))

# Slow version
np.diag(np.dot(A, B))

# Fast version
np.sum(A * B.T, axis=1)

# Faster version
np.einsum("ij,ji->i", A, B)

#### 70. Consider the vector [1, 2, 3, 4, 5], how to build a new vector with 3 consecutive zeros interleaved between each value? (★★★)

Z = np.array([1,2,3,4,5])
nz = 3
Z0 = np.zeros(len(Z) + (len(Z)-1)*(nz))
Z0[::nz+1] = Z
print(Z0)