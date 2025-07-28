import torch

# 初始化参数
w1, w2, w3, w4 = 0.2, -0.4, 0.5, 0.6
w5, w6, w7, w8 = 0.1, -0.5, -0.3, 0.8

# 输入和权重张量
X = torch.tensor([0.5, 0.3], dtype=torch.float32)  # 输入层 (1x2)
W1 = torch.tensor([[w1, w2],
                   [w3, w4]], dtype=torch.float32)  # 输入层到隐藏层权重 (2x2)
W2 = torch.tensor([[w5, w6],
                   [w7, w8]], dtype=torch.float32)  # 隐藏层到输出层权重 (2x2)

# 前向传播
h_input = torch.matmul(X, W1)
o=torch.matmul(h_input, W2)# 隐藏层输入 (1x2)
   # 输出层结果 (1x2)

print("PyTorch输出 (y1, y2):", o)