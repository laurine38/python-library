Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import pandas as pd
from pandas import*
s = pd.Series([12, -4, 7, 9])
s
0    12
1    -4
2     7
3     9
dtype: int64
s = pd.Series([12, -4, 7, 9],index=['a', 'b', 'c', 'd'])
s
a    12
b    -4
c     7
d     9
dtype: int64
s[2]
7
s['c']
7
s[1] = 0
s
a    12
b     0
c     7
d     9
dtype: int64
s['d'] = 1
s
a    12
b     0
c     7
d     1
dtype: int64
serd = pd.Series([1, 0, 2, 1, 2, 3], index=['white', 'white', 'blue', 'green','green', 'yellow'])
serd
white     1
white     0
blue      2
green     1
green     2
yellow    3
dtype: int64
data = {'Country': ['Belgium', 'India', 'Brazil'], 'Capital':['Brussels', 'New Delhi', 'Brasilia'], 'Popoulation':[11190846, 1303171035, 207847528]}
df = pd.DataFrame(data, columns=['Country', 'Capital', 'Population'])
df
   Country    Capital Population
0  Belgium   Brussels        NaN
1    India  New Delhi        NaN
2   Brazil   Brasilia        NaN
data = {'color' :['blue', 'green', 'yellow', 'red', 'white'], 'object' :['ball', 'pen', 'pencil', 'paper', 'mug'], 'price' : [1.2, 1.0, 0.6, 0.9, 1.7]}
frame = pd.DataFrame(data)
frame
    color  object  price
0    blue    ball    1.2
1   green     pen    1.0
2  yellow  pencil    0.6
3     red   paper    0.9
4   white     mug    1.7
frame.index.name = 'id'
frame.columns.name = 'item'
frame
item   color  object  price
id                         
0       blue    ball    1.2
1      green     pen    1.0
2     yellow  pencil    0.6
3        red   paper    0.9
4      white     mug    1.7
frame = pd.DataFrame(np.arange(16).reshape((4, 4)), index=['red', 'blue', 'yellow', 'white'], columns=['ball', 'pen', 'pencil', 'paper'])
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    frame = pd.DataFrame(np.arange(16).reshape((4, 4)), index=['red', 'blue', 'yellow', 'white'], columns=['ball', 'pen', 'pencil', 'paper'])
NameError: name 'np' is not defined
import pandas as pd
import numpy as np
from pandas import*
csvframe = pd.read_csv('ch05_01.csv')
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    csvframe = pd.read_csv('ch05_01.csv')
  File "C:\Users\windowz10\AppData\Roaming\Python\Python310\site-packages\pandas\util\_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\windowz10\AppData\Roaming\Python\Python310\site-packages\pandas\io\parsers\readers.py", line 586, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\windowz10\AppData\Roaming\Python\Python310\site-packages\pandas\io\parsers\readers.py", line 482, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\windowz10\AppData\Roaming\Python\Python310\site-packages\pandas\io\parsers\readers.py", line 811, in __init__
    self._engine = self._make_engine(self.engine)
  File "C:\Users\windowz10\AppData\Roaming\Python\Python310\site-packages\pandas\io\parsers\readers.py", line 1040, in _make_engine
    return mapping[engine](self.f, **self.options)  # type: ignore[call-arg]
  File "C:\Users\windowz10\AppData\Roaming\Python\Python310\site-packages\pandas\io\parsers\c_parser_wrapper.py", line 51, in __init__
    self._open_handles(src, kwds)
  File "C:\Users\windowz10\AppData\Roaming\Python\Python310\site-packages\pandas\io\parsers\base_parser.py", line 222, in _open_handles
    self.handles = get_handle(
  File "C:\Users\windowz10\AppData\Roaming\Python\Python310\site-packages\pandas\io\common.py", line 702, in get_handle
    handle = open(
FileNotFoundError: [Errno 2] No such file or directory: 'ch05_01.csv'
