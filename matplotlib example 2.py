Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3)
[<matplotlib.lines.Line2D object at 0x000001F2147D0D00>]
ax.scatter([0.3, 3.8, 1.2, 2.5], [11, 25, 9, 26], color='darkgreen', marker='^')
<matplotlib.collections.PathCollection object at 0x000001F2147D0FD0>
ax.set_xlim(0.5, 4.5)
(0.5, 4.5)
plt.show()
