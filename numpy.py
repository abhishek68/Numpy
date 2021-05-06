# -*- coding: utf-8 -*-
"""
Created on Thu May  6 12:14:01 2021

@author: ABHISHEK
"""
import numpy as np

lst1=[12.23 , 13.32 , 100 ,36.32]
print("Original list:",lst1)
print("One-dimensional NumPy array:",np.array(lst1))
print(np.arange(2, 11).reshape(3,3))
x=np.arange(12,38)
print("Original array:")
print(x)
print("Reversed array:")
print(x[::-1])
array1 = np.array([10,10,20,20,20,30,30])
print("Array1: ",array1)
array2 = [10, 20, 30]
print("Array2: ",array2)
print("Common values between two arrays:")
print(np.intersect1d(array1, array2))
x = np.array([10, 10, 20, 20, 30, 30])
print("Original array:")
print(x)
print("Unique elements of the above array:")
print(np.unique(x))
x = np.array([[1, 1], [2, 3]])
print("Original array:")
print(x)
print("Unique elements of the above array:")
print(np.unique(x))
print(np.diag([1, 2, 3, 4, 5]))
a = np.arange(10,22).reshape((3, 4))
print("Original array:")
print(a)
print("Each element of the array is:")
for x in np.nditer(a):
  print(x,end=" ")
print()
print("Multiply")
array4=np.array([[1,2,3],[3,2,1]])
array5=np.array([[3,2,1],[1,2,3]])
result=np.multiply(array4,array5)
print(result)