import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import matplotlib.image as image


# Fixing random state for reproducibility
np.random.seed(19680801)

datafile = cbook.get_sample_data('logo2.png', asfileobj=False)
print('loading %s' % datafile)
im = image.imread(datafile)
im[:, :, -1] = 0.5  # set the alpha channel


matplotlib.rcParams['axes.unicode_minus'] = False
fig, ax = plt.subplots()
ax.plot(np.random.rand(20), 'o', ms=0, lw=0, alpha=0.7, mfc='orange')
ax.plot(10*np.random.randn(100), 10*np.random.randn(100), 'o')

ax.grid()
fig.figimage(im, 10, 10, zorder=3)


ax.set_title('Using hyphen instead of Unicode minus')

plt.show()
