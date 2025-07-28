import numpy as np

# 初始化参数
w1, w2, w3, w4 = 0.2, -0.4, 0.5, 0.6
w5, w6, w7, w8 = 0.1, -0.5, -0.3, 0.8

# 输入和权重矩阵
X = np.array([0.5, 0.3])  # 输入层 (1x2)
W1 = np.array([[w1, w2],
               [w3, w4]])  # 输入层到隐藏层权重 (2x2)
W2 = np.array([[w5, w6],
               [w7, w8]])  # 隐藏层到输出层权重 (2x2)

# 前向传播
h_input = np.dot(X, W1)       # 隐藏层输入 (1x2)
h = 1 / (1 + np.exp(-h_input)) # Sigmoid激活 (1x2)
output = np.dot(h, W2)         # 输出层结果 (1x2)

print("Numpy输出 (y1, y2):", output)