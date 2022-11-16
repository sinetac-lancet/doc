'''
-*- coding: utf-8 -*-
@File  : draw.py
@author: dutengfei
@title: title
@Time  : 2022/11/16 22:48
'''
import numpy as np
import matplotlib.pyplot as plt

# X = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7']
# Y = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7']
#
# harvest = np.array([[0.56, 0.23, 6.9, 3.9, 0.0, 4.0, 0.0],
#                     [2.4, 0.0, 4.0, 1.0, 2.7, 0.0, 0.0],
#                     [1.1, 2.4, 0.8, 4.3, 1.9, 4.4, 0.0],
#                     [0.6, 0.0, 0.3, 10, 3.1, 0.0, 0.0],
#                     [0.7, 1.7, 0.6, 2.6, 2.2, 6.2, 0.0],
#                     [1.3, 1.2, 0.0, 0.0, 0.0, 3.2, 5.1],
#                     [0.1, 2.0, 0.0, 1.4, 0.0, 1.9, 6.3]])
# plt.xticks(np.arange(len(X)), label=X, rotation=45, rotation_mode="anchor", ha="right")
# plt.yticks(np.arange(len(Y)), label=Y, rotation=45, rotation_mode="anchor", ha="right")
#
# for i in range(len(X)):
#     for j in range(len(Y)):
#         text = plt.text(j, i, harvest[i, j], ha="center", va="center", color="w")
#
# plt.imshow(harvest)
# plt.tight_layout()
# plt.colorbar()
# plt.show()
# plt.close()


data = np.random.randint(1, 680, size=(13, 17))
X = np.arange(0, 13, 1)
Y = np.arange(0, 17, 1)
plt.xticks(np.arange(len(X)), label=X, rotation=45, rotation_mode="anchor", ha="right")
plt.yticks(np.arange(len(Y)), label=Y, rotation=45, rotation_mode="anchor", ha="right")

for i in range(len(X)):
    for j in range(len(Y)):
        text = plt.text(j, i, data[i, j], ha="center", va="center", color="w")

plt.imshow(data)
plt.tight_layout()
plt.colorbar()
plt.show()
plt.close()
