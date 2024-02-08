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