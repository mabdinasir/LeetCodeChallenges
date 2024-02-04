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
print(Z)

#### 8. Reverse a vector (first element becomes last) (★☆☆)
Z = np.arange(50)
Z = Z[::-1]
print(Z)

#### 9. Create a 3x3 matrix with values ranging from 0 to 8 (★☆☆)
Z = np.arange(9).reshape(3, 3)
print(Z)

#### 10. Find indices of non-zero elements from [1,2,0,0,4,0] (★☆☆)
nz = np.nonzero([1,2,0,0,4,0])
print(nz)
