import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

import time

hour = time.strftime("%H")
print hour
minute = time.strftime("%M")
print minute
second = time.strftime("%S")
print second
    
n=10
p=0.3
k=np.arange(0,21)
binomial = stats.binom.pmf(k,n,p)
print binomial[1]
plt.plot(k,binomial,'o-')
plt.title('Binomial: n=%i, p=%.2f'%(n,p),fontsize=15)
plt.show()
