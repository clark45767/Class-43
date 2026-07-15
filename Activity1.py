import numpy as np 
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

print(arr[0])
print(arr[2])
print(arr[1:5])
print(arr.dtype)

arr1 = np. array([4, 7, 1, 5, 4, ], dtype='S')
print(arr1)
print(arr1.dtype)

arr2 = np.array([[4, 8, 5],
                [ 1, 2, 3, ]])
print(arr2.shape)

print(arr2)

arr3 = np.array([2,4,6,3,4,7,7,8,65,2,7,2,3,5,6,9])
print(arr3)
print(arr3.reshape(4,4))