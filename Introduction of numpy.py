Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy as np

a = np.array([1, 2, 3])
a
array([1, 2, 3])
c = np.array([[1, 2, 3],[4, 5, 6]])
c
array([[1, 2, 3],
       [4, 5, 6]])
e = np.array([(1, 2, 3),(4, 5, 6),(7, 8, 9)])
e
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
g = np.array([['a', 'b'],['c', 'd']])
g
array([['a', 'b'],
       ['c', 'd']], dtype='<U1')
f = np.array([[1,2,3],[4, 5, 6]], dtype=complex)
f
array([[1.+0.j, 2.+0.j, 3.+0.j],
       [4.+0.j, 5.+0.j, 6.+0.j]])
np.ones((3, 3))
array([[1., 1., 1.],
       [1., 1., 1.],
       [1., 1., 1.]])
np.zeros((2, 2))
array([[0., 0.],
       [0., 0.]])
np.arange(0, 10)
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
np.arange(5, 10)
array([5, 6, 7, 8, 9])
np.arange(0, 12, 3)
array([0, 3, 6, 9])
np.arange(0, 6, 0.6)
array([0. , 0.6, 1.2, 1.8, 2.4, 3. , 3.6, 4.2, 4.8, 5.4])
np.arange(0, 12).reshape(3, 4)
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
np.linespace(0,10,5)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    np.linespace(0,10,5)
  File "C:\Users\windowz10\AppData\Roaming\Python\Python310\site-packages\numpy\__init__.py", line 313, in __getattr__
    raise AttributeError("module {!r} has no attribute "
AttributeError: module 'numpy' has no attribute 'linespace'. Did you mean: 'linspace'?
np.linspace(0,10,5)
                         
array([ 0. ,  2.5,  5. ,  7.5, 10. ])
np.random.random(3)
                         
array([0.4996958 , 0.67063415, 0.64499712])
np.random.random((3, 3))
                         
array([[0.60803119, 0.76842673, 0.00814125],
       [0.13480508, 0.62029903, 0.14555065],
       [0.28868323, 0.39920895, 0.51143505]])
