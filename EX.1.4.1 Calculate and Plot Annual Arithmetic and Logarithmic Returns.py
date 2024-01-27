# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 09:55:20 2024

@author: giane
"""

import numpy as np
import matplotlib . pyplot as plt

values=np.array([10.0 , 12.5 , 8.0 , 13.5 , 7.5 , 15.0])


arithmetic_returns=(values[1:]-values[: -1])/values[: -1]
log_returns=np.log(values [1:]/values[: -1])


plt.plot(arithmetic_returns, label='Arithmetic Returns', marker='o')
plt.plot(log_returns, label='Logarithmic Returns', marker='x')
plt . title ('Annual Arithmetic vs. Logarithmic Returns ')
plt . xlabel ('Year' )
plt . ylabel ('Returns ')
plt.show


cumulative_arithmetic_return= np.cumsum(arithmetic_returns)
cumulative_logarithmic_return=np.exp(np.cumsum(log_returns))-1


plt.plot(cumulative_arithmetic_return,label='Cumulative Arithmetic Returns', marker ='o')
plt.plot(cumulative_logarithmic_return,label='Cumulative Logarithmic Returns',marker ='x')
plt.title ('Cumulative Arithmetic vs. Logarithmic Returns')
plt.xlabel ('Year')
plt.ylabel ('Cumulative Returns')
plt . show ()
