import numpy as np 

print(f"Zeros: \n{np.zeros(10, dtype=int)}")
print(f"Ones: \n{np.ones((5,5), dtype=float)}")
print(f"Full: \n{np.full((4,5), 3.14)}")
print(f"Arange: \n{np.arange(0,20,2)}")
print(f"Linspace: \n{np.linspace(0,1,5)}")
print(f"Random: \n{np.random.random((3,3))}")
print(f"Normal: \n{np.random.normal((3,3))}")
print(f"Identity: \n{np.eye(4)}")
print(f"Uninitilized array: \n{np.empty((3,3))}")

# numpy array attributes
np.random.seed(0)
x = np.random.randint(10, size=(3,4))
x1 = np.array([[i for i in range(10**2)] for j in range(10)])
# print("x1: ", x1)
print("Dim: ", x1.ndim)
print("Shape: ", x1.shape)
print("size: ", x1.size)
print("Dtype: ", x1.dtype)
print("itemsize: ", x1.itemsize)
print("nbytes: ", x1.nbytes)

# array indexing
x = np.array([5,0,3,3,7,9])
print(f"x[3]: {x[3]}")
print("x[-1]: ",x[-1])
x2 = np.array([[3,5,2,4],
               [7,6,8,8],
               [1,6,7,7]])
print("x[2,1]: ",x2[2,1])

# array slicing

x = np.arange(0,40,2)
print("x[3:10:2]: ", x[3:10:2]) # x[from:to:everynthelement]
x = np.random.randint(10, size=(5,6))
print('x: ',x)
print("x[:,:2]: ", x[:,:2])
print("x.reshape(3,10): ", x.reshape((3,10)))

x= np.array([1,2,3])
print("x[np.newaxis,:]: ", x[np.newaxis,:])
print("x[:,np.newaxis]: ", x[:,np.newaxis])

x = np.array([2,1,4,3,5])
%timeit print("Sorted array: ", np.sort(x))
