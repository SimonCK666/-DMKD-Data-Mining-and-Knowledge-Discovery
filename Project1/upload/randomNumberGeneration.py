'''
Author: SimonCK666 SimonYang223@163.com
Date: 2022-11-05 23:25:00
LastEditors: SimonCK666 SimonYang223@163.com
LastEditTime: 2022-11-07 11:08:52
FilePath: /Project1/randomNumberGeneration.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%A
'''
import numpy as np
import matplotlib.pyplot as plot
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
import pandas as pd
from sklearn import preprocessing
from scipy.stats import norm
from scipy import stats

'''
1-1.1	Generate three streams (1D, 2D) of random numbers with 1,000 samples
'''
stream1D = np.random.randint(0, 100, size = [1000, 1])
print(stream1D.shape)
stream2D = np.random.randint(0, 100, size = [1000, 2])
print(stream2D.shape)


'''
1-1.2	Visualize the generated samples, you may use a scatterplot.
'''
# generate a 1D scatterpoint graph
plot.scatter(stream1D, np.zeros_like(stream1D) + 0)
plot.title("1D stream scatterpoint graph")
plot.show()

# generate a 2D scatterpoint graph
plot.scatter(stream2D[:,0],stream2D[:,1])
plot.title("2D stream scatterpoint graph")
plot.show()


'''
1-1.3 & 4	Compute & Visualize the histogram of the three streams, then normalize them to become a probability density function (pdf).
'''
# histogram and pdf of 1D data
sns.distplot(stream1D[:,0], color='g')
plot.title("histogram and pdf of 1D stream")
plot.show()

# histogram and pdf of 2D data
sns.distplot(stream2D[:,0], color='g')
sns.distplot(stream2D[:,1], color='b')
plot.title("histogram and pdf of 2D stream")
plot.show()
