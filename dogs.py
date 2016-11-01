import matplotlib  # this will make the histogramm display (on my linux system)
matplotlib.use('TkAgg') #same thing

import numpy as np
import matplotlib.pyplot as plt

# This program will display a histogram
# showing two dog breeds' height,
# grey(red) and lab(blue),


greyhounds = 500
labradors = 500

greyHeights = 28 + 4 * np.random.randn(greyhounds)
labHeights = 24 + 4 * np.random.randn(labradors)

plt.hist([greyHeights,labHeights], stacked = True, color = ['r', 'b'])
plt.show()


