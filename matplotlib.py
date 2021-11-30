Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100)

plt.plot(x, x, label='linear')
[<matplotlib.lines.Line2D object at 0x000001F29CF90DF0>]
plt.legend
<function legend at 0x000001F29B70C5E0>
plt.show()
