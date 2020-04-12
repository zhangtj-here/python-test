import  matplotlib.pyplot as plt
#
# # 绘制简单的曲线
# # plt.plot([1, 3, 5], [4, 8, 10],[2, 5, 10])
# plt.plot([1, 3, 5], [4, 8, 10])
# plt.show()

import numpy as np

import pandas as pd
# x = np.linspace(-np.pi,np.pi,100) # x轴的定义为 -3.14-3.14，中间间隔100个元素
# plt.plot(x,np.sin(x))
# plt.show()


# x = np.linspace(-np.pi * 2, np.pi * 2, 100) # x轴的定义为 -3.14-3.14，中间间隔100个元素
# plt.figure(1, dpi=50) # 創建图表1,dpi代表图片精细度，dpi越大文件越大，杂志要300以上
# for i in range(1, 5): # 画四条线
#     plt.plot(x, np.sin(x / i))
# plt.show()

# plt.figure(1, dpi=50)
# data = [1, 1, 1, 2, 2, 2, 3, 3, 5, 5, 6, 5, 5]
# plt.hist(data) # 只要传入数据，直方图就会统计数据出现的次数
# plt.show()

# x = np.arange(1,10)
# y = x
# fig = plt.figure()
# plt.scatter(x,y,c = 'r',marker= 'o') #c = 'r'表示散点的颜色为红色，marker 表示指定三点多形状为圆形
# plt.show()
import warnings
import seaborn as sns

iris = pd.read_csv('./iris_training.csv')
sns.set(style="white", color_codes=True)
# sns.jointplot(x="120", y="4", data=iris, size=5)
# sns.distplot(iris['120'])
# print(iris.head())

sns.FacetGrid(iris, hue="virginica", size=5).map(plt.scatter, '120', '4').add_legend()
sns.FacetGrid(iris, hue="virginica", size=5).map(plt.scatter, "setosa", "versicolor").add_legend()
# iris.plot(kind="scatter", x="120", y="4")
plt.show()